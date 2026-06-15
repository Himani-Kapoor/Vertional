from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Honey Ki jai Ho')

def userList(request):
    return render(request,'userlist.html')
