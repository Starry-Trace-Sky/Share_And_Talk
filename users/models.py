from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

import uuid


class Profile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          verbose_name="UUID", auto_created=True)
    nickname = models.CharField(max_length=20, verbose_name="昵称", 
                                unique=True)
    #avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    avatar = models.URLField(max_length=500, default="https://sdn.geekzu.org/avatar/?size=40",
                             verbose_name="头像链接")
    
    REQUIRED_FIELDS = ['nickname']
    
    class Meta:
        db_table = 'db_users'
        ordering = ['id']
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.nickname
