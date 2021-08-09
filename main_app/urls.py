from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('main_app.api.urls')),
]