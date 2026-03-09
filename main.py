from src.yt import searchByTopic
from src.yt import extract

example = {'kind': 'youtube#searchListResponse', 
           'etag': '7H_1vI9pLMsMM8w-qKmFeH_PB0U', 
           'nextPageToken': 'CAEQAA', 
           'regionCode': 'US', 'pageInfo': {'totalResults': 1000000, 'resultsPerPage': 1}, 
           'items': 
                [{'kind': 'youtube#searchResult', 
                  'etag': 'J_xjOk8-Z523EoDjz9g_ZHhWKnA', 
                  'id': {'kind': 'youtube#video', 
                         'videoId': '8aYr2ueCFvs'}, 
                         'snippet': {'publishedAt': '2022-06-06T21:35:35Z', 
                                     'channelId': 'UCNRl8nOCoUvki2FNFxQZgEg', 
                                     'title': 'HOW CRYPTOCURRENCY WORKS  💸💶', 
                                     'description': 'shorts Me and my investment in bitcoin.', 
                                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/8aYr2ueCFvs/default.jpg', 
                                    'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/8aYr2ueCFvs/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/8aYr2ueCFvs/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': 'dednahype', 'liveBroadcastContent': 'none', 'publishTime': '2022-06-06T21:35:35Z'}}]}



def main():
    re = searchByTopic("bitcoin", 2)
    extra_store = re
    pr = extract(re)
    print(pr)
    print(extra_store)

if __name__ == "__main__":
    main()


