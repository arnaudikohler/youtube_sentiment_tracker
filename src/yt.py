from src.config import YOUTUBE_API_KEY
from googleapiclient.discovery import build

def searchByTopic(topic, max_results):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=topic,
        part="snippet",
        type="video",
        order="viewCount",
        maxResults=max_results
    )

    response = request.execute()

    return response