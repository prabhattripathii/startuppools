from urllib.parse import urlparse
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ServiceFun)
]
