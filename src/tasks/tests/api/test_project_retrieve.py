import pytest


pytestmark = [pytest.mark.django_db]


def test_get_by_owner(client, project, project_detail_url):
    resp = client.get(project_detail_url)
    data = resp.data

    assert resp.status_code == 200
    assert data['id'] == project.pk
    assert data['title'] == project.title


def test_get_by_admin(admin, project, project_detail_url):
    resp = admin.get(project_detail_url)
    data = resp.data

    assert resp.status_code == 200
    assert data['id'] == project.pk
    assert data['title'] == project.title


def test_get_by_another_user(another_client, project, project_detail_url):
    resp = another_client.get(project_detail_url)

    assert resp.status_code == 403


def test_get_by_anon(anon, project, project_detail_url):
    resp = anon.get(project_detail_url)

    assert resp.status_code == 401
