import pytest
from django.urls import reverse


@pytest.fixture
def self_url():
    return reverse('users:self')


@pytest.fixture
def register_url():
    return reverse('users:register')


@pytest.fixture
def change_password_url():
    return reverse('users:change_password')
