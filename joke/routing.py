from django.urls import path

from .consumer import JokeConsumer

ws_urlpatterns = [
    path('ws/jokes/', JokeConsumer.as_asgi()),
]
