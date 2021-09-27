import pytest

from tasks.models import Project


pytestmark = [pytest.mark.django_db]


def test_delete_by_owner(client, project, project_detail_url):

    assert Project.objects.count() == 1

    resp = client.delete(project_detail_url)

    assert resp.status_code == 204
    assert Project.objects.count() == 0


def test_delete_by_admin(admin, project, project_detail_url):

    assert Project.objects.count() == 1

    resp = admin.delete(project_detail_url)

    assert resp.status_code == 204
    assert Project.objects.count() == 0


def test_delete_by_another_user(another_client, project, project_detail_url):
    resp = another_client.delete(project_detail_url)

    assert resp.status_code == 403


def test_delete_by_anon(anon, project, project_detail_url):
    resp = anon.delete(project_detail_url)

    assert resp.status_code == 401
