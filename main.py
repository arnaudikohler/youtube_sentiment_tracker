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
    
    out = searchByTopic("bitcoin", 5)
    out2 = extract_Title_Desc(out)
    print(out2)
    out3 = captionExtractor(out2)
    out4 = captionConverter(out3)
    out5 = addCaptionToTitleDesc(out2, out4)
    out6 = sentimentCalc(out5)
    print(out6)
    print(out5)
    print(proportionSentiments(out6))
    print(meanSentiments(out6))

    btc = yf.Ticker("BTC-USD")
    price = btc.history(period="1d")["Close"].iloc[-1]  

    create_table()

    today = date.today().isoformat()

    insert_sentiment(
        today,
        "bitcoin",
        meanSentiments(out6),
        proportionSentiments(out6),
        price
    )

    # with open("data/test_search_response.json") as f:
    #     response = json.load(f)
    
    # with open("data/captions.json", "r") as f2:
    #     content = [json.loads(line) for line in f2]
    
    # out = extract_Title_Desc(response)
    # out3 = captionConverter(content)
    # out4 = addCaptionToTitleDesc(out, out3)
    # print(out4)
    # print(out3)
    # out2 = sentimentCalc(out4)
    # print(out2)
    # print(proportionSentiments(out2))
    # print(meanSentiments(out2))

if __name__ == "__main__":
    main()


    