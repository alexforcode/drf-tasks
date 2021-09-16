import pytest

from users.models import User


pytestmark = [pytest.mark.django_db]


def test_ok(anon, register_url):
    password = 'c3por2d2'
    data = {
        'email': 'luke@starwars.com',
        'username': 'luke',
        'password': password,
        'password2': password,
    }

    resp = anon.post(register_url, data)

    assert resp.status_code == 201

    user = User.objects.get(email='luke@starwars.com')

    assert user


def test_passwords_not_equal(anon, register_url):
    data = {
        'email': 'luke@starwars.com',
        'username': 'luke',
        'password': 'c3por2d2',
        'password2': 'c3por2d3',
    }

    resp = anon.post(register_url, data)

    assert resp.status_code == 400
