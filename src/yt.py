from src.config import YOUTUBE_API_KEY
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import time
import random
from datetime import datetime, timedelta, timezone

def searchByTopic(topic, max_results):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=topic,
        part="snippet",
        type="video",
        order="viewCount",
        publishedAfter = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        maxResults=max_results
    )

    response = request.execute()

    return response

def extract_Title_Desc(video_list): 
    result = [] 
    for i in video_list["items"]: 
        result.append({
            "title": i["snippet"]["title"],
            "description": i["snippet"]["description"],
            "video_id": i["id"]["videoId"]
        })
    return result

def captionExtractor(video_list):
    result = []
    ytt_api = YouTubeTranscriptApi()
    for video in video_list:
        try:
            transcript_list = ytt_api.list(video["video_id"])
            try:
                transcript = transcript_list.find_manually_created_transcript(['en'])
            except:
                try:
                    transcript = transcript_list.find_generated_transcript(['en'])
                except:
                    transcript = next(iter(transcript_list))
            captions = transcript.fetch().to_raw_data()
            result.append(captions[:50])
            time.sleep(random.uniform(3,5))
        except Exception as e:
            print("Exception:", e, {type(e).__name__})
            result.append(None)
    return result

def captionConverter(li): 
    result = []
    for video in li: 
        if video is not None:
            captions = []
            for segment in video: 
                captions.append(
                    segment["text"]
                )
            result.append(" ".join(captions))
        else:
            result.append(0)
    return result

def addCaptionToTitleDesc(li, captions):
    for video, cap in zip(li, captions):
        video["captions"] = cap
    return li
    