import random
import string

import pytest
from mixer.backend.django import mixer

from core.test.api_client import DRFClient


@pytest.fixture
def password():
    return ''.join([random.choice(string.hexdigits + string.digits) for _ in range(10)])


@pytest.fixture
def user(password):
    user = mixer.blend('users.User')
    user.set_password(password)
    user.save()

    return user


@pytest.fixture
def another_user(password):
    user = mixer.blend('users.User')
    user.set_password(password)
    user.save()

    return user


@pytest.fixture
def admin():
    return DRFClient(admin=True)


@pytest.fixture
def client(user):
    return DRFClient(user)


@pytest.fixture
def another_client(another_user):
    return DRFClient(another_user)


@pytest.fixture
def anon():
    return DRFClient(anon=True)
