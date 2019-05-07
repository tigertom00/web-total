from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from users.forms import CustomUserCreationForm


def root(request):
    return render(request, 'root.html')
