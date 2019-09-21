from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def roomlist(request):
    return render(request, 'chat/room_list.html', {})

def login(request):
    return render(request, 'chat/login.html', {})

def usercreate(request):
    return render(request, 'chat/user_create', {})