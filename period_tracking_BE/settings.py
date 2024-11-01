"""
Django settings for period_tracking_BE project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from os import getenv as os_getenv
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os_getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# allowed hosts
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'cycles',
    'users',
    'predictions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware'
    # 'period_tracking_BE.middlewares.RateLimitMiddleware',
    'middlewares.auth_middleware.AuthMiddleware',
    'middlewares.exception_middleware.ExceptionMiddleware',
    # 'period_tracking_BE.middlewares.ResponseMiddleware',
]

ROOT_URLCONF = 'period_tracking_BE.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'period_tracking_BE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'period_tracking',
        'ENFORCE_SCHEMA': True, 
        'CLIENT': {
            'host': 'mongodb://mongodb:27017/',
        },
        'CONN_MAX_AGE' : None,
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'rate_limit',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "loguru": {
            "class": "utils.logger.InterceptHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["loguru"], "level": "INFO"},
    }
}

# REST_FRAMEWORK = {
#     # # ... other settings ...
#     # 'DEFAULT_RENDERER_CLASSES': [
#     #     'period_tracking_BE.middlewares.CustomFlexibleRenderer',
#     #     'rest_framework.renderers.BrowsableAPIRenderer',
#     # ],
#     'EXCEPTION_HANDLER': None,
# }


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#################################################################
##################### ALLOWED ENDPOINTS #########################
#################################################################
SKIP_AUTH_PATTERNS = [
    '/api/v1/auth/',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#################################################################
##################### ENVIRONMENT VARIABLES #####################
#################################################################
# APPLICATION SETTINGS
SESSION_SECRET_KEY = os_getenv('SESSION_SECRET_KEY')
SESSION_EXPIRY = int(os_getenv('SESSION_EXPIRY'))
USER_ID_HASH_SALT = os_getenv('USER_ID_HASH_SALT')

# CELERY SETTINGS
CELERY_BROKER_URL = os_getenv('CELERY_BROKER_URL')

# RATE LIMIT SETTINGS
NON_REGISTERED_RATE_LIMIT = int(os_getenv('NON_REGISTERED_RATE_LIMIT'))  
REGISTERED_RATE_LIMIT = int(os_getenv('REGISTERED_RATE_LIMIT'))  
RATE_LIMIT_WINDOW = timedelta(hours=int(os_getenv('RATE_LIMIT_WINDOW'))) 

