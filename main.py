from src.yt import searchByTopic
from src.yt import extract
from src.yt import captionExtractor
from src.yt import captionConverter
import json

def main():
    with open("data/test_search_response.json") as f:
        response = json.load(f)
    
    with open("data/captions.json", "r") as f2:
        content = [json.loads(line) for line in f2]
    
    out = extract(response)
    print(out)
    out2 = captionConverter(content)
    for i in out2:
        print("------------------")
        print("------------------")
        print("------------------")
        print(i)

if __name__ == "__main__":
    main()


