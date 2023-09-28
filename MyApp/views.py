# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("MyApp/index.html")
    context = {
        "athlete": 3,
    }
    return HttpResponse(template.render(context, request))
