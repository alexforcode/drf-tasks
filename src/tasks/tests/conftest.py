from django.urls import reverse
from mixer.backend.django import mixer
import pytest


@pytest.fixture
def project(user):
    return mixer.blend('tasks.project', user=user)


@pytest.fixture
def projects_url():
    return reverse('tasks:project-list')


@pytest.fixture
def project_detail_url(project):
    return reverse('tasks:project-detail', args=[project.pk])
