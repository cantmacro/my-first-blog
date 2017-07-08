from django.shortcuts import render
from . import apps

# Create your views here.

def get_home(request):
    data = {}
    data['news'] = {}
    data['weather'] = {}
    data['news']['sport1'] = apps.sport1reader()
    data['news']['kicker'] = apps.kickerreader()
    data['weather']['today'] = apps.weather()
    return render(request,'news/news.html',context=data)
