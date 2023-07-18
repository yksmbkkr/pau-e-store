from .base import *
from settings import env_vars

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['local.dev.yashkulshreshtha.me', 'pau-app.dev.yashkulshreshtha.me', ]

OSCAR_SEND_REGISTRATION_EMAIL = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_LOCATION = 'public/static'
AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_IS_GZIPPED = True
# AWS_S3_REGION_NAME = 'ap-south-1'
AWS_STORAGE_BUCKET_NAME = env_vars.AWS_STORAGE_BUCKET_NAME
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = env_vars.AWS_S3_ENDPOINT_URL
AWS_S3_CUSTOM_DOMAIN = env_vars.AWS_S3_CUSTOM_DOMAIN

AWS_ACCESS_KEY_ID = env_vars.AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY = env_vars.AWS_SECRET_ACCESS_KEY

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'pau_shop.storage_backends.MediaStorage'

FIREBASE_CREDS = env_vars.FIREBASE_CREDS
