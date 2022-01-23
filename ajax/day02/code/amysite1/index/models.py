from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=32)
    nickname = models.CharField(max_length=30, verbose_name="昵称")



