from allauth.account.forms import LoginForm
from django.shortcuts import redirect, reverse
from timelister.forms import JobberForm, TimelisteForm


def custom_context(request):
    navbarloginform = LoginForm(request.POST or None)

    return {
        'navbarloginform': navbarloginform
    }


# def global_jobber_form(request):
#     globaljobberform = JobberForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("new_jobb"))

#     return {
#         'globaljobberform': globaljobberform
#     }


# def global_timeliste_form(request):
#     globaltimelisteform = TimelisteForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return redirect(reverse("new_jobb"))

#     return {
#         'globaltimelisteform': globaltimelisteform
#     }
