# coding:utf8
import time
from celery import Celery

#first args is the name of the current module
#app = Celery('tasks', broker='amqp://guest@localhost//')
#app = Celery('tasks', backend='redis://121.40.208.251', broker='amqp://')
app = Celery('tasks', backend='amqp', broker='amqp://guest@121.40.208.251//')

app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)

'''
@app.task(bind=True)
def upload_files(self, filenames):
    for i, file in enumerate(filenames):
        print '*(*(*', self.state
        self.update_state(state='PROGRESS',  meta={'current': i, 'total': len(filenames)})
'''


@app.task
def add(x, y):
    #s = 1/0
    return x + y

#celery -A tasks worker --loglevel=info

def run_task1():
    result = add.delay(10, 99)
    print result.state
    print 'result = ', result
    print result.ready()
    print result.state
    print result.backend
    #print result.get(timeout=1)


if __name__ == '__main__':
    print 'start..'
    run_task1()

    '''
    result.get(propagate=False)
    print 'track: ',result.traceback
    print result.ready()
    '''
    print 'end...'