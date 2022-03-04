"""Django settings for config project."""
import os
import django_heroku
import dj_database_url
from decouple import config,Csv

MODE=config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', False)
# development
if config('MODE')=="dev":
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': config('DB_NAME'),
           'USER': config('DB_USER'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST'),
           'PORT': '',
       }
       
   }
# production
else:
   DATABASES = {
       'default': dj_database_url.config(
           default=config('DATABASE_URL')
       )
   }
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())



MODE=config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')
# development


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '5yo93-8a^%idwkzxz@6gq67p2ml#sraf4=7#pqg+28mv)koo@m'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third-party apps
    'crispy_forms',

    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'coupons.apps.CouponsConfig',
    "users",
    'social_django', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GITHUB_KEY = '2089ce4bd171db78699e'
SOCIAL_AUTH_GITHUB_SECRET = '789f6938c236cc80b200ba4eea9560a096c642cb'
SOCIAL_AUTH_URL_NAMESPACE = "social"

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


#Crispy templates for form rendering
CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'
LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = "/"
CONTACT_EMAIL = 'contact@example.com'
ADMIN_EMAILS = ['admin@example.com', ]


# Twilio SendGrid

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}
# Bottom of the file

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


#Crispy templates for form rendering
CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'
django_heroku.settings(locals())