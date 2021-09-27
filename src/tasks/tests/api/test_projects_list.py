import pytest


pytestmark = [pytest.mark.django_db]


def test_ok(client, projects_url):
    resp = client.get(projects_url)

    assert resp.status_code == 200


def test_anon(anon, projects_url):
    resp = anon.get(projects_url)

    assert resp.status_code == 401
