import firebase_admin
from django.conf import Settings
from firebase_admin import auth
from pathlib import Path
from firebase_admin import credentials

from pau_shop.settings import FIREBASE_CREDS


def get_firebase_app():
    BASE_DIR = Path(__file__).resolve().parent.parent
    GOOGLE_APPLICATION_CREDENTIALS = FIREBASE_CREDS
    cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(credential=cred)


def verify_id_token_custom(id_token):
    try:
        get_firebase_app()
        decoded_token = auth.verify_id_token(id_token=id_token, check_revoked=True)
    except auth.RevokedIdTokenError:
        return False, 'REVOKED_TOKEN'
    except auth.InvalidIdTokenError as e:
        print(e)
        return False, 'INVALID_TOKEN'
    except Exception as e:
        print(e)
        return False, 'INVALID_TOKEN'

    return True, decoded_token
