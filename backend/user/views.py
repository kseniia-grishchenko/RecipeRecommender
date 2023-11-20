from django.shortcuts import render, get_object_or_404


def user_profile(request):
    return render(request, 'user_profile.html', {'user_profile': request.user})
