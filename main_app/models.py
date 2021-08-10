from django.db import models

# Create your models here.
class YouTubeVideo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=1024)
    description = models.TextField(max_length=5000)
    channel_title = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_url = models.URLField()

    class Meta:
        verbose_name = 'YouTube Video'
        verbose_name_plural = 'YouTube Videos'

    def __str__(self):
        return self.title