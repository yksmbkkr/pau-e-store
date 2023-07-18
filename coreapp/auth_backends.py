import sys
import traceback

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.core import exceptions
from django.middleware.csrf import CsrfViewMiddleware

from coreapp.firebase_utils import verify_id_token_custom


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class FirebaseAuthBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        try:

            User = get_user_model()
            authorization_header = request.headers.get('Authorization')

            if not authorization_header:
                return None

            identifier, access_token = authorization_header.split(' ', 1)
            if not identifier == 'Token':
                raise exceptions.PermissionDenied("Invalid token prefix")

            # if username is None:
            #     username = kwargs.get('username')
            # if username is None or access_token is None or fuid is None:
            #     return

            is_access_token_valid, decoded_token = verify_id_token_custom(access_token)

            # is_access_token_valid = True
            # uid = 'testuser1'
            # if uid != fuid:
            #     is_access_token_valid = False
            uid = decoded_token['uid']
            email = decoded_token['email']
            name = decoded_token['name'].split(' ', 1)
            first_name = name[0]
            last_name = name[1] if len(name) > 1 else ''

            if is_access_token_valid:
                try:
                    user_object = User.objects.get(username=uid)
                    if not user_object.is_active:
                        raise exceptions.PermissionDenied('User is inactive')
                    return user_object
                except User.DoesNotExist:
                    user_object = User(username=uid, email=email, first_name=first_name, last_name=last_name)
                    user_object.set_unusable_password()
                    user_object.save()
                    return user_object
            else:
                return None
        except Exception as e:
            traceback.print_exception(*sys.exc_info())
            raise exceptions.PermissionDenied(e.__cause__)

    def get_user(self, user_id):
        from coreapp.models import User
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None