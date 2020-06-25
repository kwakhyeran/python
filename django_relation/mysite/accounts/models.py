from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followings",
        blank=True
    )
# 각종 필드를 추가
# createsuperuser할 수 없음, 필드 추가하기전 admin계정 만들기
# shell_plus에서 create_user is_staff, 최고권한 True
# User.objects.create_user(username='admin',password='admin',is_staff=True,is_superuser=True)