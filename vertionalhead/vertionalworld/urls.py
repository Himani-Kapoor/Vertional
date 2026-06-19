from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('login/', views.login, name='login'),
    path('userlist/', views.userList, name='userlist'),

]
