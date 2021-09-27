import random
import string

import pytest


pytestmark = [pytest.mark.django_db]


def test_ok(client, password, change_password_url):
    new_password = ''.join([random.choice(string.hexdigits + string.digits) for _ in range(10)])
    data = {
        'old_password': password,
        'new_password': new_password,
    }

    resp = client.put(change_password_url, data)

    assert resp.status_code == 204


def test_same_password(client, password, change_password_url):
    data = {
        'old_password': password,
        'new_password': password,
    }

    resp = client.put(change_password_url, data)

    assert resp.status_code == 400
    assert resp.data['new_password'][0] == 'New password is the same as old.'


def test_wrong_old_password(client, change_password_url):
    wrong_password = ''.join([random.choice(string.hexdigits + string.digits) for _ in range(10)])
    new_password = ''.join([random.choice(string.hexdigits + string.digits) for _ in range(10)])
    data = {
        'old_password': wrong_password,
        'new_password': new_password,
    }

    resp = client.put(change_password_url, data)

    assert resp.status_code == 400
    assert resp.data['old_password'][0] == 'Old password is not correct.'

