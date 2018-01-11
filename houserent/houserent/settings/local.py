from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')j87lqt&fr*#4m(i8*jz*6$jkjg4jt*z%su#nfb=&p0zg$kzsf'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
