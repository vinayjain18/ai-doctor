from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
import logging

logger = logging.getLogger()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username != None and password != None:
            # Get the user
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    logger.info('User is authenticated, logging user in')
                    return user
            except User.DoesNotExist:
                pass
        return None



"""
try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class CustomAuth(ModelBackend):
    def authenticate(**credentials):
        return super(CustomAuth, self).authenticate(**credentials)

    def authenticate(self, username=None, password=None):    
        # Check the username/password and return a User.
        if username != None and password != None:
            # Get the user
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    logger.info('User is authenticated, logging user in')
                    return user
            except User.DoesNotExist:
                pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
           return None
"""