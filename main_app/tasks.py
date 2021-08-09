from celery import shared_task
from datetime import datetime, timedelta
import requests
from celery.schedules import crontab

from django.conf import settings

from .models import YouTubeVideo

@shared_task
def fetch_yt_videos():
    yt_search_api_url = 'https://www.googleapis.com/youtube/v3/search'
    search_query = 'tech'

    last_saved_video = YouTubeVideo.objects.order_by("-published_at").first()

    if last_saved_video:
        publishedAfter = last_saved_video.published_at + timedelta(seconds=1)
    else:
        publishedAfter = datetime.now() - timedelta(days=5)

    params = {
        'part': 'snippet',
        'q': search_query,
        'max_results': 20,
        'order': 'date',
        'type': 'video',
        'publishedAfter': publishedAfter.strftime(settings.YOUTUBE_DATETIME_FORMAT),
    }

    for api_key in settings.YOUTUBE_DATA_API_KEYS.split(','):
        params["key"] = api_key
        response = requests.get(yt_search_api_url, params)

        if response.status_code == 403:
            # Quota exceeded
            print("Quota exceeded for one of the key.")
        else:
            break

    if response.status_code == 403:
        print("Quota exceeded for all keys")
        return

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
