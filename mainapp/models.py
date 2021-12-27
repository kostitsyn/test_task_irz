from django.db import models
from uuid import uuid4


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64, verbose_name='Name')
    last_name = models.CharField(max_length=128, verbose_name='Surname')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Question(models.Model):
    creation_date = models.DateField(auto_now_add=True, verbose_name='Date of creation')
    title = models.CharField(max_length=256, verbose_name='Task title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_answered = models.BooleanField(default=False, db_index=True, verbose_name='Is it question answered')
    link = models.URLField(verbose_name='link to question')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['-creation_date']
