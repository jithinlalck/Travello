from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.

def fnIndex(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,'index.html', {'result':obj,'result1':obj1})


def fnServices(request):
    return render(request,'services.html')

def fnNews(request):
    return render(request,'news.html')

def fnContact(request):
    return render(request,'contact.html')

def fn_about(request):
    return render(request,'about.html')
def fn_home(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})

