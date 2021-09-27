import pytest

from tasks.models import Project


pytestmark = [pytest.mark.django_db]


def test_update_by_owner(client, project, project_detail_url):
    data = {
        'title': 'Updated title',
        'description': 'Updated description',
    }
    resp = client.put(project_detail_url, data)

    updated_project = Project.objects.get(id=project.pk)

    assert resp.status_code == 200
    assert updated_project.title == data['title']


def test_update_by_admin(admin, project, project_detail_url):
    data = {
        'title': 'Updated title',
        'description': 'Updated description',
    }
    resp = admin.put(project_detail_url, data)

    updated_project = Project.objects.get(id=project.pk)

    assert resp.status_code == 200
    assert updated_project.title == data['title']


def test_update_by_another_user(another_client, project, project_detail_url):
    data = {
        'title': 'Updated title',
        'description': 'Updated description',
    }
    resp = another_client.put(project_detail_url, data)

    assert resp.status_code == 403


def test_update_by_anon(anon, project, project_detail_url):
    data = {
        'title': 'Updated title',
        'description': 'Updated description',
    }
    resp = anon.put(project_detail_url, data)

    assert resp.status_code == 401
