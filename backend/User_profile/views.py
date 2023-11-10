from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'user_profile.html', {'user_profile': user_profile})


