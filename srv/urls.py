from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', views.root, name='root'),
    path('messages/', include('postman.urls', namespace='postman')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('jobb/', include('jobb.urls')),
    path('timelister/', include('timelister.urls')),
    path('matriell/', include('matriell.urls')),
    path('members/', include('members.urls')),
    path('testing/', include('testing.urls')),

]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

# accounts / ^ ^ signup /$ [name = 'account_signup']
# accounts / ^ ^ login /$ [name = 'account_login']
# accounts / ^ ^ logout /$ [name = 'account_logout']
# accounts / ^ ^ password/change /$ [name = 'account_change_password']
# accounts / ^ ^ password/set /$ [name = 'account_set_password']
# accounts / ^ ^ inactive /$ [name = 'account_inactive']
# accounts / ^ ^ email /$ [name = 'account_email']
# accounts / ^ ^ confirm-email /$ [name = 'account_email_verification_sent']
# accounts / ^ ^ confirm-email/(?P < key > [-:\w]+) /$ [name = 'account_confirm_email']
# accounts / ^ ^ password/reset /$ [name = 'account_reset_password']
# accounts / ^ ^ password/reset/done /$ [name = 'account_reset_password_done']
# accounts / ^ ^ password/reset/key/(?P < uidb36 > [0-9A-Za-z]+)-(?P < key > .+)
#  /$ [name = 'account_reset_password_from_key']
# accounts / ^ ^ password/reset/key/done /$ [name = 'account_reset_password_from_key_done']
# accounts / ^social/
# accounts / ^github/
