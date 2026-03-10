from src.yt import searchByTopic
from src.yt import extract_Title_Desc
from src.yt import captionExtractor
from src.yt import captionConverter
# from src.nlp import sentimentizer
import json



def main():
    
    with open("data/test_search_response.json") as f:
        response = json.load(f)
    
    with open("data/captions.json", "r") as f2:
        content = [json.loads(line) for line in f2]
    
    out = extract_Title_Desc(response)
    print(out)

    for i in out:
        print(i["title"])

if __name__ == "__main__":
    main()


