# -*- coding: utf-8 -*-
from .settings import *
__author__ = 'H.A.V.S'

with open(os.path.join(BASE_DIR, 'codepm.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
    'werkzeug',
    'debug_toolbar'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pm_db',
        'USER': 'root',
        'PASSWORD': 'A8d32e08.',
    }
}

STATIC_ROOT = ''

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static"),
]