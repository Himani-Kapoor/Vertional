from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Honey Ki jai Ho')
