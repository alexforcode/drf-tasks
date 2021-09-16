from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        'Email',
        unique=True,
        help_text='Required. Must be unique.',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        name = f'{self.first_name} {self.last_name}'

        if len(name) < 3:
            return f'{self.username}'

        return name.strip()
