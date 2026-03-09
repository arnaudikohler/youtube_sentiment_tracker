from src.yt import searchByTopic
from src.yt import extract
from src.yt import captionExtractor
import json

def main():
    with open("data/test_search_response.json") as f:
        response = json.load(f)
    
    out = extract(response)
    out2 = captionExtractor(out)
    print(out2)

if __name__ == "__main__":
    main()


