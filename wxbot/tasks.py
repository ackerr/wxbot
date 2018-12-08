from celery_config import app as celery_app
from constants import Constants, Username
from main import get_friend, get_group, itchat
from weather import get_weather


@celery_app.task
def send_something(msg, name):
    itchat.send(msg, toUserName=get_friend(name))


@celery_app.task
def send_weather():
    weather = []
    for city in Constants.WEATHER_CITY:
        weather.append(get_weather(city))
    weather = '\n\n'.join(weather)
    itchat.send(weather, toUserName=get_group(Username.FRIEND_GROUP))
