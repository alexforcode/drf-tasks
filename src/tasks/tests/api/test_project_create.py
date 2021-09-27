import pytest

from tasks.models import Project


pytestmark = [pytest.mark.django_db]


def test_create_by_user(client, user, projects_url):
    data = {
        'title': 'Test title',
        'description': 'Test description',
    }
    resp = client.post(projects_url, data)

    project = Project.objects.all().first()

    assert resp.status_code == 201
    assert project.user == user


def test_create_by_anon(anon, projects_url):
    data = {
        'title': 'Test title',
        'description': 'Test description',
    }
    resp = anon.post(projects_url, data)

    assert resp.status_code == 401
