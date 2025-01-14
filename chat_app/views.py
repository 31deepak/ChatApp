from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chat/chat.html", {"users": users})
