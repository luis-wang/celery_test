from django.shortcuts import render
from tasks import add
# Create your views here.

def invoke_celery(request):
    add.delay(91, 2)
    print 'ran.......'
