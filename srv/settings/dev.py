from .base import *

SECRET_KEY = 'moazn*&+f)6sr5er9@=g&$qj!plnan809p^=%f^^95!ch$h^or'

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
