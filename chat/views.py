from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.utils.safestring import mark_safe
# Create your views here.
# chat/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

@login_required
def room(request, room_name): # room_name is taken by url sent by a index.html 
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),

    })
