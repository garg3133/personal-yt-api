from ..models import YouTubeVideo
from .serializers import YouTubeVideoSerializer

from rest_framework import generics, filters


class SearchAPIView(generics.ListAPIView):
    queryset = YouTubeVideo.objects.order_by("-published_at")
    serializer_class = YouTubeVideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']