from src.config import YOUTUBE_API_KEY
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

def searchByTopic(topic, max_results):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=topic,
        part="snippet",
        type="video",
        order="relevance",
        maxResults=max_results
    )

    response = request.execute()

    return response


def extract(video_list):
    result = []
    for i in video_list["items"]:
        result.append((
            i["snippet"]["title"],
            i["snippet"]["description"],
            i["id"]["videoId"]
        ))

    return result

def captionExtractor(video_id):
    result = []
    ytt_api = YouTubeTranscriptApi()
    for i in video_id:
        try: 
            result.append(
                ytt_api.fetch(i[2])
            )
        except Exception as e:
            result.append(
                None
            )
    print(result)