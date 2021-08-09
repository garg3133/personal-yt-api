from django.urls import path

from . import views

urlpatterns = [
    path('videos/search/', views.SearchAPIView.as_view(), name='search'),
]
