from datetime import timedelta

from celery import Celery

app = Celery('tasks', backenk='redis://localhost', broker='pyamqp://')

app.conf.update(
    timezone='Asia/Shanghai',
    beat_schedule={
        'morning_task': {
            'task': 'tasks.morning_task',
            'schedule': timedelta(seconds=10),
            'args': ('Hello World',)
        }
    }
)


@app.task
def morning_task(msg):
    return msg
