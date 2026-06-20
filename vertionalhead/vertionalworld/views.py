from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import SumForm
from .models import Watch


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
    is_watching = False
    if request.user.is_authenticated:
        is_watching = Watch.objects.filter(user=request.user, target='store').exists()

    context = {"data": sum, "is_watching": is_watching}
    return render(request,'store.html',context)

def userList(request):
    return render(request,'userlist.html')


@require_POST
@login_required
def subscribe_store(request):
    target = 'store'
    watch, created = Watch.objects.get_or_create(user=request.user, target=target)
    return JsonResponse({'watching': True, 'created': created})


@require_POST
@login_required
def unsubscribe_store(request):
    target = 'store'
    Watch.objects.filter(user=request.user, target=target).delete()
    return JsonResponse({'watching': False})


def watch_status(request):
    if not request.user.is_authenticated:
        return JsonResponse({'watching': False})
    watching = Watch.objects.filter(user=request.user, target='store').exists()
    return JsonResponse({'watching': watching})
