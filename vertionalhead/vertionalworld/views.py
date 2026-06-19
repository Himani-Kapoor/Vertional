from django.shortcuts import render
from django.http import HttpResponse
from .forms import SumForm


# Create your views here.

def home(request):
    return render(request,'home.html')
def login(request):
    result = None
    if request.method == 'POST':
        form = SumForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            def logic(x, y):
                return x + y
            result = logic(a, b)
    else:
        form = SumForm()

    context = {'form': form, 'result': result}
    return render(request, 'login.html', context)

def store(request):
    def logic(a,b):
        c=a+b
        return c
    sum=logic(10,2)
    

    context = {"data": sum}
    return render(request,'store.html',context)

def userList(request):
    return render(request,'userlist.html')
