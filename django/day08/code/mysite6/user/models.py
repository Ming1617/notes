from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=30)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return "用户" + self.username