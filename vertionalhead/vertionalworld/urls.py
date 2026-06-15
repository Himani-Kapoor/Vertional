from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from views import home
from django.urls import path, include

urlpatterns = [
    path('', home, name='home')

]
