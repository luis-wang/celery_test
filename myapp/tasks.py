# coding:utf8
import time
from celery import Celery

#first args is the name of the current module
#app = Celery('tasks', broker='amqp://guest@localhost//')
#app = Celery('tasks', backend='redis://localhost', broker='amqp://')
app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)



@app.task
def add(x, y):
    #s = 1/0
    return x + y

#celery -A tasks worker --loglevel=info

if __name__ == '__main__':
    print 'start..'
    result = add.delay(100, 99)
    print 'result = ', result
    #print result.get(timeout=1)
    result.get(propagate=False)
    print 'track: ',result.traceback
    print result.ready()
    print 'end...'