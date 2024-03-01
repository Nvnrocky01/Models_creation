from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
def topic(request):
    qlto=Topic.objects.all()
    d={'topic':qlto}
    return render(request,'topic.html',d)



def webpage(request):
    qlwo=Webpage.objects.all()
    d={'webpage':qlwo}
    return render(request,'webpage.html',d)


def acessRecord(request):
    qlao=AcessRecord.objects.all()
    d={'webpage':qlao}
    return render(request,'acessrecord.html',d)


def insert_topic(request):
    tn=input()
    tno=Topic.objects.get_or_create(topic_name=tn)[0]
    tno.save() 
    return render(request,'topic.html')



def insert_webpage(request):
    tn=input()
    n=input()
    u=input()
    to=Topic.objects.get(topic_name=tn)
    wpo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wpo.save()
    return render(request,'webpage.html')



def insert_acessrecord(request): 
    pk=int(input())
    a=input()
    d=input()

    WO=Webpage.objects.get(pk=pk)
    NAO=AcessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()

    return HttpResponse('data')

    