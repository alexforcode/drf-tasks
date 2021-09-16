import random
import string

import pytest
from django.urls import reverse
from mixer.backend.django import mixer


@pytest.fixture
def self_url():
    return reverse('users:self')


@pytest.fixture
def register_url():
    return reverse('users:register')


@pytest.fixture
def change_password_url():
    return reverse('users:change_password')


@pytest.fixture
def password():
    return ''.join([random.choice(string.hexdigits + string.digits) for _ in range(10)])


@pytest.fixture
def user(password):
    user = mixer.blend('users.User')
    user.set_password(password)
    user.save()

    return user
