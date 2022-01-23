from django.db import models

# Create your models here.

#出版社是一对多中的‘一’
class Publisher(models.Model):
    name=models.CharField(max_length=50,
                          verbose_name='出版社')
    def __str__(self):
        return '出版社：'+self.name

class Book2(models.Model):
    title=models.CharField(max_length=30,
                           verbose_name='书名')
    pub =models.ForeignKey(Publisher,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '书名2：'+self.title
