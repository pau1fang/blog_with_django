from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.urls import reverse


class BlogUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=150, blank=True)
    avatar_hash = models.CharField(max_length=32)
    created_time = models.DateTimeField('创建时间', default=now)
    modify_time = models.DateTimeField('修改时间', default=now)

    def get_absolute_url(self):
        return reverse('blog:author_detail', kwargs={'author_name': self.username})

    def __str__(self):
        return self.nickname


