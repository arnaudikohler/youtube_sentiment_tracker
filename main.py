from src.yt import searchByTopic
from src.yt import extract_Title_Desc
from src.yt import captionExtractor
from src.yt import captionConverter, addCaptionToTitleDesc
from src.nlp import sentimentCalc, proportionSentiments, meanSentiments
from src.db import create_table, insert_sentiment
from datetime import date
import yfinance as yf
import json



def main():
    
    sresults_btc = searchByTopic("bitcoin", 10)
    videos = extract_Title_Desc(sresults_btc)
    print(videos)
    raw_captions = captionExtractor(videos)
    caption_txt = captionConverter(raw_captions)
    videos_with_captions = addCaptionToTitleDesc(videos, caption_txt)
    sentiment_scores = sentimentCalc(videos_with_captions)
    print(sentiment_scores)
    print(proportionSentiments(sentiment_scores))
    print(meanSentiments(sentiment_scores))

    btc = yf.Ticker("BTC-USD")
    price = btc.history(period="1d")["Close"].iloc[-1]  

    create_table()

    today = date.today().isoformat()

    insert_sentiment(
        today,
        "bitcoin",
        meanSentiments(sentiment_scores),
        proportionSentiments(sentiment_scores),
        price
    )

if __name__ == "__main__":
    main()


    