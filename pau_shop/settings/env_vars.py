import os


def get_env(key):
    return os.environ[key]

AWS_STORAGE_BUCKET_NAME = get_env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = get_env('AWS_S3_ENDPOINT_URL')
AWS_S3_CUSTOM_DOMAIN = get_env('AWS_S3_CUSTOM_DOMAIN')
AWS_ACCESS_KEY_ID = get_env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env('AWS_SECRET_ACCESS_KEY')

FIREBASE_CREDS = {
  "type": "service_account",
  "project_id": get_env('project_id'),
  "private_key_id": get_env('private_key_id'),
  "private_key": get_env('private_key'),
  "client_email": get_env('client_email'),
  "client_id": get_env('client_id'),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": get_env('client_x509_cert_url'),
  "universe_domain": "googleapis.com"
}

SECRET_KEY = get_env('SECRET_KEY')