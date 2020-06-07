"""

Django settings for nexus project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '70*r*0cg1sqoa__$e=5yt9v5$d7z7b^fwivo6^1k%#gn9!ck3p'

# SECURITY WARNING: don't run with debug turned on in production!
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
    'register',
    'home',
	'userprofile',
    'post',
    'search',
    'crispy_forms',
    'chat',
    'channels', 
    'widget_tweaks',
    'django_private_chat',
]



CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nexus.urls'
# Channels
ASGI_APPLICATION = "nexus.routing.application"  #after this we no longer using WSGI 

# channel layer can communicate with Redis now.
# adding redis support to the channel
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


TEMPLATES =[

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Nexus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#      'default': { 
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mate_dev1',  #schema name is mate_dev
# 		'USER': 'root',
# 		'PASSWORD':'aa44bd80sr',
# 		'HOST': 'localhost',
# 		'PORT': '3306',
# 		}
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}







# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'





# note:Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

#------------------------------------------
STATIC_ROOT=    os.path.join(BASE_DIR, 'boot') #bootstrap
#------------------------------------------


LOGIN_REDIRECT_URL="/home/"

LOGOUT_REDIRECT_URL="/"

CRISPY_TEMPLATE_PACK = 'bootstrap4'