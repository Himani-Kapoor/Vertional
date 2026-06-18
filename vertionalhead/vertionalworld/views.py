from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')

def store(request):
    context = {"data": "Passing Argument To Template"}
    return render(request,'store.html',context)

def userList(request):
    return render(request,'userlist.html')
