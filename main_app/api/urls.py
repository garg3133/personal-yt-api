from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.GetAPIView.as_view(), name='videos_get_api'),
    path('videos/search/', views.SearchAPIView.as_view(), name='videos_search_api'),
]
