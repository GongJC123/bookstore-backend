from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):

    mobile = models.CharField("手机号", max_length=11)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

