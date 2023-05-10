from django.contrib.auth.backends import BaseBackend
from .models import xzz_user_login  # import your custom user model

class MyAuthBackend(BaseBackend):
    def authenticate(self, email=None, password=None):
        try:
            user = xzz_user_login.objects.get(email=email)

            if password == getattr(user, 'password'):
                #auth success
                return user
            else:
                return False
        except xzz_user_login.DoesNotExist:
            return None

    #use email to log in system
    def get_user(self, email):
        try:
            return xzz_user_login.objects.get(email=email)
        except xzz_user_login.DoesNotExist:
            return None