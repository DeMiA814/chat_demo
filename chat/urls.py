from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('roomlist', views.roomlist, name='room_list'),
    path('login', views.login, name='login'),
    path('user_create', views.usercreate, name='user_create'),
]