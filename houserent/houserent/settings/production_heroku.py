from .base import *     # noqa
import dj_database_url

# 把 debug 模式關掉。
DEBUG = False

# 設定 secret key。
SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')
#DJANGO_SECRET_KEY = 'j0@^%7*-_#1p+r8id(o@r=zuq4ts%66_aii)jjax3'
#SECRET_KEY = 'j0@^%7*-_#1p+r8id(o@r=zuq4ts%66_aii)jjax3'

# 尊重 HTTPS 連線中的 "X-Forwarded-Proto" header。
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 設定靜態檔位置。
STATIC_ROOT = 'static'

# 設定資料庫。
DATABASES = {
    'default': dj_database_url.config()
}

# 允許所有網址連至本網站。
ALLOWED_HOSTS = ['*']
