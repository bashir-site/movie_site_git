import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'k7vzrjs0@@imqc1n@^pj56tna$md+96sl^%!az564k4v@il=p3'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST':'localhost',
        'PORT': '5432',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')