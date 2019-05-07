from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')


def profile(request):
    return render(request, 'users/profile.html')
