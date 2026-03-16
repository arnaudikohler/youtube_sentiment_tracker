from src.yt import searchByTopic
from src.yt import extract_Title_Desc
from src.nlp import sentimentCalc, proportionSentiments, meanSentiments, weightedSentiment
from src.db import create_table, insert_sentiment, create_table_raw, insert_raw
from datetime import date
import yfinance as yf

# ("nvidia", "NVDA")
# ("bitcoin", "BTC-USD")

def main():

    topics = [
        ("bitcoin", "BTC-USD"),
        ("nvidia", "NVDA")
    ]

    today = date.today().isoformat()

    # ---- create tables once ----
    create_table()
    create_table_raw()

    for topic, ticker in topics:

        print(f"\nProcessing topic: {topic}")

        sresults = searchByTopic(topic, 30)
        videos = extract_Title_Desc(sresults)

        # ---- compute raw sentiment components ----
        sentiment_components = sentimentCalc(videos)

        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]

        # ---- insert raw per-video data ----
        for v in sentiment_components:
            insert_raw(
                today,
                topic,
                v["video_id"],
                v["title_score"],
                v["description_score"],
                v["caption_score"]
            )

        # ---- weight experiments ----
        weight_tests = [
            ("title_focus", 0.9, 0.1, 0),
            ("balanced", 0.5, 0.5, 0),  
            ("title_only", 1.0, 0, 0)
        ]

        for name, tw, dw, cw in weight_tests:

            sentiment_scores = weightedSentiment(
                sentiment_components,
                titleWeight=tw,
                descWeight=dw,
                captionWeight=cw
            )

            print(f"\nWeight scheme: {name}")
            print("scores:", sentiment_scores)
            print("positive ratio:", proportionSentiments(sentiment_scores))
            print("mean sentiment:", meanSentiments(sentiment_scores))

            insert_sentiment(
                today,
                topic,
                meanSentiments(sentiment_scores),
                proportionSentiments(sentiment_scores),
                price,
                tw,
                dw,
                cw
            )


if __name__ == "__main__":
    main()