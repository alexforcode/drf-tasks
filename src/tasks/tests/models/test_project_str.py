from mixer.backend.django import mixer
import pytest


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    ('title', 'description', 'expected'),
    [
        ('Test', 'Description', 'Test'),
        ('Test', '', 'Test'),
    ],
)
def test(title, description, expected):
    project = mixer.blend('tasks.Project', title=title, description=description)

    assert str(project) == expected
