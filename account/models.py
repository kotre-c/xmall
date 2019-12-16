from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField('邮箱', max_length=20, null=True)
    image = models.ImageField('图片', max_length=100, upload_to='media/img/user/', null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "mobile": self.mobile,
            "image": self.image
        }
