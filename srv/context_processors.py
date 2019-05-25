from allauth.account.forms import LoginForm
from commands.city_weather import city_weather


def custom_context(request):
    navbarloginform = LoginForm(request.POST or None)
    weather = city_weather

    return {
        'weather': weather,
        'navbarloginform': navbarloginform
    }
