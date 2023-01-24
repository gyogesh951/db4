from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QST=Webpage.objects.all()
    d={'webpage':QST}
    return render(request,'display_webpage.html',d)

