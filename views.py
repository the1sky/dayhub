__author__ = 'dumingtan'

from django.http import HttpResponse, Http404
from django.db import connection
import datetime

def hello(request):
    return HttpResponse('hello world')

def homepage(request):
    return HttpResponse( 'welcome to my home' )

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>it is now %s.</body></html>' %now
    return HttpResponse( html )

def hours_ahead(request, offset):
    try:
        offset = int( offset )
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset, dt)

    return HttpResponse( html )

def mysql(request):
    cursor = connection.cursor()
    return HttpResponse( 'mysql' )