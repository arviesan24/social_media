"""
Django settings for social_media project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json

from django.urls import reverse_lazy

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'SECRET_KEY', '4dwe^ro^_2_gp2z7u^z=zx!_f%7vxqexy5t)k-p2y)3s@ksyo)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = json.loads(os.getenv('DEBUG', 'false'))

ALLOWED_HOSTS = json.loads(
    os.getenv('ALLOWED_HOSTS', '["localhost", "127.0.0.1", "[::1]"]')) # don't forget to update `USE_HTTPS` and `CURRENT_DOMAIN` too for APIs


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project apps
    'accounts',
    'comments',
    'posts',

    #third party apps
    'django_filters',
    'django_summernote',
    'rest_framework',
    'rest_framework.authtoken',
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

ROOT_URLCONF = 'social_media.urls'

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
                'social_media.context_processors.global_template_variables',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_media.wsgi.application'


#
# PROTOCOL TO USE
#

USE_HTTPS = json.loads(os.getenv('USE_HTTPS', 'true'))

CURRENT_PROTOCOL = 'http://'

if USE_HTTPS:
    CURRENT_PROTOCOL = 'https://'


#
# DOMAIN NAME TO USE
#

CURRENT_DOMAIN = os.getenv('CURRENT_DOMAIN', '127.0.0.1:8000/')


#
# API ROOT URL
#

API_ROOT_URL = f'{CURRENT_PROTOCOL}{CURRENT_DOMAIN}api/'


#
# REST_FRAMEWORK SETTINGS
#

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}


#
# SUMMERNOTE CUSTOMIZATION
#

SUMMERNOTE_THEME = 'bs4'

SUMMERNOTE_CONFIG = {
    'width': '100%',
    'height': '300',
}


#
# DEFINE CUSTOM USER MODEL
#

AUTH_USER_MODEL = 'accounts.User'


#
# LOGIN SETTINGS
#

# login url to redirect for `LoginRequiredMixin`
LOGIN_URL = reverse_lazy('accounts:login')
# redirect user to create profile to check if profile already exists after login
LOGIN_REDIRECT_URL = reverse_lazy('accounts:create-profile')


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

STATIC_ROOT = os.getenv(
    'STATIC_ROOT',
    os.path.join(BASE_DIR, 'public', 'static'))

STATIC_URL = os.getenv('STATIC_URL', '/static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = os.getenv('MEDIA_URL', '/media/')

MEDIA_ROOT = os.getenv(
    'MEDIA_ROOT',
    os.path.join(BASE_DIR, 'public', 'media'))
