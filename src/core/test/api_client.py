import random
import string

from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class DRFClient(APIClient):
    def __init__(self, user=None, admin=False, anon=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.admin = admin

        if not anon:
            self.auth()

    def auth(self):
        self.user = self.user or self._create_user(self.admin)

        token = RefreshToken.for_user(self.user).access_token
        self.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

    def _create_user(self, admin=True):
        user_opts = {}

        if admin:
            user_opts = {
                'is_staff': True,
                'is_superuser': True,
            }

        user = mixer.blend('users.User', **user_opts)
        self.password = ''.join([random.choice(string.hexdigits + string.digits) for _ in range(6)])
        user.set_password(self.password)
        user.save()

        return user

    def logout(self):
        self.credentials()
        super().logout()
