from allauth.account.forms import LoginForm
from commands.city_weather import city_weather


def custom_context(request):
    navbarloginform = LoginForm(request.POST or None)

    return {
        'weather': lambda: city_weather,
        'navbarloginform': navbarloginform
    }
