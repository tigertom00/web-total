import os
from decouple import config

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(
                __file__))))

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'testing',
    'users',
    'jobb',
    'timelister',
    'matriell',
    'members',

    'postman',
    # 'ajax_select',
    # 'notification',
    # 'mailer',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'flatpickr',
    'easy_thumbnails',
    'bootstrap_modal_forms',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'srv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'srv.context_processors.custom_context',
                'postman.context_processors.inbox',
            ],
        },
    },
]

WSGI_APPLICATION = 'srv.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django AllAuth config && Auth Config

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'root'
LOGOUT_REDIRECT_URL = 'root'

# AllAuth

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_USERNAME_MIN_LENGTH = 4

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Easy Thumbnail

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (30, 30), 'crop': True},
        'jobb_thumbs': {'size': (75, 75), 'crop': True},
        'profile_picture': {'size': (300, 300), 'crop': True},
    },
}

# Postman

POSTMAN_AUTO_MODERATE_AS = True
# POSTMAN_I18N_URLS = True  # default is False
POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
# POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
# POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
# POSTMAN_DISABLE_USER_EMAILING = True  # default is False
# POSTMAN_FROM_EMAIL = 'from@host.tld'  # default is DEFAULT_FROM_EMAIL
# POSTMAN_PARAMS_EMAIL = get_params_email  # default is None
# POSTMAN_AUTO_MODERATE_AS = True  # default is None
# POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
# POSTMAN_NAME_USER_AS = 'last_name'  # default is None
# POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
# POSTMAN_NOTIFIER_APP = None  # default is 'notification'
# POSTMAN_MAILER_APP = None  # default is 'mailer'
# POSTMAN_AUTOCOMPLETER_APP = {
# 'name': '',  # default is 'ajax_select'
# 'field': '',  # default is 'AutoCompleteField'
# 'arg_name': '',  # default is 'channel'
# 'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
# }  # default is {}
