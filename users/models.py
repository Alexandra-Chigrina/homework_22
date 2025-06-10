from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон',
                                    help_text='Введите номер телефона')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна', help_text='Введите страну')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
