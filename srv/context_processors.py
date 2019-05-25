from allauth.account.forms import LoginForm
from commands import city_weather


def custom_context(request):
    navbarloginform = LoginForm(request.POST or None)

    return {
        'weather': city_weather.city_weather,
        'navbarloginform': navbarloginform
    }
