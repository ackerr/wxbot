import time
import datetime
import requests

from threading import Timer
from weather import get_weather


def morning_notice():
    hour = datetime.datetime.now().hour
    if hour == 22:
        ans = get_weather('萧山')
        return ans


def get_news():
    # 这里是把今日糍粑每日一句中拿过来的信息发送给你朋友
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news(friend, msg):
    news = get_news()
    friend.send(news[0] + '\n' + news[1])
    friend.send('今日天气' + '\n' + msg)
    t = Timer(60, send_news, args=(friend, msg))  # 86400是间隔时间（一天）
    t.start()


if __name__ == '__main__':
    contents, note = get_news()
    print(note)
    print(int(time.time()))
    print()
    print(type(datetime.time(hour=22)))
    print(datetime.datetime.now().minute)

    # while True:
    #     time = datetime.datetime.now()
    #     if time.hour == 15 and time.minute == 0 and time.second == 0:
    #         weather = get_weather('萧山')
    #         print(weather)
    #         break
