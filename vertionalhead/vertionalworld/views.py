from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')

def store(request):
    def logic(a,b):
        c=a+b
        return c
    sum=logic(10,2)
    

    context = {"data": sum}
    return render(request,'store.html',context)

def userList(request):
    return render(request,'userlist.html')
