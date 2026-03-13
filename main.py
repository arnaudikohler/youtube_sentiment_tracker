from src.yt import searchByTopic
from src.yt import extract_Title_Desc
from src.yt import captionExtractor
from src.yt import captionConverter, addCaptionToTitleDesc
from src.nlp import sentimentCalc, proportionSentiments, meanSentiments, weightedSentiment
from src.db import create_table, insert_sentiment, create_table_raw, insert_raw
from datetime import date
import yfinance as yf


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

        sresults = searchByTopic(topic, 10)
        videos = extract_Title_Desc(sresults)

        raw_captions = captionExtractor(videos)
        caption_txt = captionConverter(raw_captions)
        videos_with_captions = addCaptionToTitleDesc(videos, caption_txt)

        # ---- compute raw sentiment components ----
        sentiment_components = sentimentCalc(videos_with_captions)

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
            ("baseline", 0.7, 0.15, 0.15),
            ("title_focus", 0.9, 0.05, 0.05),
            ("balanced", 0.33, 0.33, 0.34),
            ("caption_focus", 0.2, 0.2, 0.6),
            ("title_desc", 0.6, 0.4, 0.0)
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