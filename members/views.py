from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model

User = get_user_model()


@permission_required('members.can_view_Test')
def secret(request):

    return render(request, 'members/secret.html')
