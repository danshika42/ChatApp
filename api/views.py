from django.shortcuts import render
from .models import UserColor

# Create your views here.
def index(request):
    return render(request, "api/index.html")

def room(request, room_name):
    user_color = UserColor.objects.get(user=request.user)
    col = user_color.col
    return render(request, "api/room.html", {"room_name": room_name,"col":col})