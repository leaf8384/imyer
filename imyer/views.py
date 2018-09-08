from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello ViVi!")

def current_datetime(request, hours_ahead = 0):
    now = datetime.datetime.now() + datetime.timedelta(hours = int(hours_ahead))
    if(hours_ahead == 0):
        html = "<html><body>It is now %s.</body></html>" %now
    else:
        html = "<html><body>In %s hours, It will be %s.</body></html>" % (hours_ahead, now)
    return HttpResponse(html)
