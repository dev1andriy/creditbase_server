"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import SESSION_ENGINE

from main.middlewares import DisableCSRF

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lzhcszxqs*i!h)c((5^(p&te(mi7q3kp&(um5%u5192yd+di)w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS = ['*']
ALLOWED_HOSTS = ['*']
# AUTH_LDAP_START_TLS = False
# LDAP_AUTH_CONNECTION_USERNAME = 'cn=read-only-admin,dc=example,dc=com'
# LDAP_AUTH_CONNECTION_PASSWORD = 'password'
# AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend", "main.SettingsBackend.SettingsBackend")
# LDAP_AUTH_URL = "ldap://ldap.forumsys.com:389"
# LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
# LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
# LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"
# LDAP_AUTH_USER_LOOKUP_FIELDS = ('username',)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

# LDAP_AUTH_SEARCH_BASE = "ou=mathematicians,dc=example,dc=com"
#
# LDAP_AUTH_USER_FIELDS = {
#     "username": "uid",
# }

# Application definition

INSTALLED_APPS = [
    # 'django_python3_ldap',
    'corsheaders',
    'main',
    'common',
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middlewares.DisableCSRF',

]

SWAGGER_SETTINGS = {

    'USE_SESSION_AUTH': False,

    'api_version': '0.1',

    'enabled_methods': [

        'get',

        'post',

    ],

    'SECURITY_DEFINITIONS': {

        "api_key": {

            "type": "apiKey",

            "name": "Authorization",

            "in": "header"

        },

    },

}

# SESSION_COOKIE_DOMAIN = 'at.main.com'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'csrfmiddlewaretoken',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'creditbase',
        'USER': 'creditbase',
        'PASSWORD': 'creditbase',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SESSION_COOKIE_HTTPONLY = False

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# SESSION_ENGINE = 'main.session.custom_session'
