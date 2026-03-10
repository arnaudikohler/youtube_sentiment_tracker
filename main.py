from src.yt import searchByTopic
from src.yt import extract_Title_Desc
from src.yt import captionExtractor
from src.yt import captionConverter, addCaptionToTitleDesc
from src.nlp import sentimentCalc, proportionSentiments, meanSentiments
import json



def main():
    
    with open("data/test_search_response.json") as f:
        response = json.load(f)
    
    with open("data/captions.json", "r") as f2:
        content = [json.loads(line) for line in f2]
    
    out = extract_Title_Desc(response)
    # print(out)
    out3 = captionConverter(content)
    out4 = addCaptionToTitleDesc(out, out3)
    # print(out4)
    # print(out3)
    out2 = sentimentCalc(out4)
    print(out2)

    print(proportionSentiments(out2))
    print(meanSentiments(out2))

if __name__ == "__main__":
    main()


