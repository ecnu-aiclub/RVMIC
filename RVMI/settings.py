from .dev import *

DEBUG = False
ALLOWED_HOSTS = ['localhost',]
ST_SITE_URL = 'http://49.52.10.133:8090/'
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'aiclub_ecnu@126.com'
EMAIL_HOST_PASSWORD = 'KIZYPUXINCXVJDJW'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ST_MATH_JAX = True
ST_NGRAM_SEARCH = True
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
