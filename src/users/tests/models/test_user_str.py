from mixer.backend.django import mixer
import pytest


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    ('first_name', 'last_name', 'expected'),
    [
        ('Luke', 'Skywalker', 'Luke Skywalker'),
        ('Luke', '', 'Luke'),
        ('', 'Skywalker', 'Skywalker'),
    ],
)
def test(first_name, last_name, expected):
    user = mixer.blend('users.User', first_name=first_name, last_name=last_name)

    assert str(user) == expected


def test_username_is_used_by_default():
    user = mixer.blend('users.User', first_name='', last_name='')

    assert str(user) == user.username
