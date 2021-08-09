from celery import shared_task
from datetime import datetime, timedelta
import requests
from celery.schedules import crontab

from django.conf import settings

from .models import YouTubeVideo

@shared_task
def fetch_yt_videos():
    print("hello")  
    yt_search_api_url = 'https://www.googleapis.com/youtube/v3/search'

    last_saved_video = YouTubeVideo.objects.order_by("-published_at").first()

    if last_saved_video:
        publishedAfter = last_saved_video.published_at + timedelta(seconds=1)
    else:
        publishedAfter = datetime.now() - timedelta(days=5)

    params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet',
        'q': 'tech',
        'max_results': 5,
        'order': 'date',
        'type': 'video',
        'publishedAfter': publishedAfter.strftime(settings.YOUTUBE_DATETIME_FORMAT),
    }

    response = requests.get(yt_search_api_url, params)
    video_result = response.json()["items"]

    videos = []
    for video in video_result:
        video_dict = {
            'id': video["id"]["videoId"],
            'title': video["snippet"]["title"],
            'description': video["snippet"]["description"],
            'channel_title': video["snippet"]["channelTitle"],
            'published_at': video["snippet"]["publishedAt"],
            'thumbnail_url': video["snippet"]["thumbnails"]["high"]["url"],
        }
        yt_video_object = YouTubeVideo(**video_dict)

        videos.append(yt_video_object)

    YouTubeVideo.objects.bulk_create(videos)
