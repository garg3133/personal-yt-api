from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.GetAPIView.as_view(), name='videos'),
    path('videos/search/', views.SearchAPIView.as_view(), name='videos_search'),
]
