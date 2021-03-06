from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend as DjangoModelBackend


class ModelBackend(DjangoModelBackend):
    def authenticate(self, request=None, username=None, password=None):
        """Username is case insensitive."""
        try:
            user = User.objects.get(username__iexact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
