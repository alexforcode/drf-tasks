import pytest


pytestmark = [pytest.mark.django_db]


def test_ok(client, self_url):
    resp = client.get(self_url)
    data = resp.data

    assert resp.status_code == 200
    assert data['id'] == client.user.pk
    assert data['email'] == client.user.email


def test_anon(anon, self_url):
    resp = anon.get(self_url)

    assert resp.status_code == 401
