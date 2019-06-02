from .base import *

SECRET_KEY = 'LKJFH=#"Q()Q¤R/=#")¤ØLKjflskfo382y3f0823fnoihewn2f238'

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(VENV_PATH, 'email')
