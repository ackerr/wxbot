from celery import Celery
from celery.schedules import crontab
from constants import Greetings, Username


app = Celery('__name__', broker='pyamqp://')

app.conf.update(accept_content=['pickle', 'json'])
app.conf.update(imports=['tasks'])

app.conf.update(
    timezone='Asia/Shanghai',
    beat_schedule={
        'say_something': {
            'task': 'tasks.send_something',
            'schedule': crontab(hour=8, minute=00),
            'args': (Greetings.MORNING, Username.GIRL_FRIEND),
        },
        'time_to_send_weather': {
            'task': 'tasks.send_weather',
            'schedule': crontab(hour=7, minute=30),
        },
    },
)
