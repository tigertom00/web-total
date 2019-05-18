from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(VENV_PATH, 'email')


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_H')
# EMAIL_PORT = 465
# EMAIL_HOST_USER = config('EMAIL_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
# EMAIL_USE_SSL = True
