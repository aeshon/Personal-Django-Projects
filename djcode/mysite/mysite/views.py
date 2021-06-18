from django.http import HttpResponse
import datetime
from django.template.loader import get_template

def hello(request):
    return HttpResponse("Hello World")

def dateTime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    context = {'current_date': now}
    return HttpResponse(t.render(context, request))

def hoursAhead(request, id):
    offset = int(id)
    return HttpResponse("Hours ahead DT = " + str(datetime.datetime.now()+datetime.timedelta(hours=offset)))