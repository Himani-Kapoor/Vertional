from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('store/subscribe/', views.subscribe_store, name='subscribe_store'),
    path('store/unsubscribe/', views.unsubscribe_store, name='unsubscribe_store'),
    path('store/watch-status/', views.watch_status, name='watch_status'),
    path('login/', views.login, name='login'),
    path('userlist/', views.userList, name='userlist'),

]
