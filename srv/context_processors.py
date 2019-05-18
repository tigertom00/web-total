from allauth.account.forms import LoginForm


def custom_context(request):
    navbarloginform = LoginForm(request.POST or None)

    return {
        'navbarloginform': navbarloginform
    }
