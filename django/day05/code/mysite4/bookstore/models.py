from django.db import models

# Create your models here.


"""
1. Book - 图书
    1. title - CharField 书名,非空,唯一
    2. pub - CharField 出版社,字符串,非空
    3. price - 图书定价,,
    4. market_price - 图书零售价
    """
class Book(models.Model):
    title=models.CharField(max_length=30,
                           db_index=True,
                           null=False,
                           unique=True,
                           verbose_name='书名')# varchar(30)
    pub=models.CharField(max_length=50,
                         null=False,
                         verbose_name='出版社',
                         default=''
                         )
    price=models.DecimalField(decimal_places=2,
                              max_digits=7,
                              default=8888,
                              verbose_name='定价',) #Decimal(7,2)
    market_price=models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='零售价',
        default='9999'
    )
    def __str__(self):
        return '书名：'+self.title

"""
Author - 作者
    1. name - CharField 姓名,非空
    2. age - IntegerField, 年龄,非空，缺省值为1
    3. email - EmailField, 邮箱,允许为空
"""
class Author(models.Model):
    name=models.CharField(
        max_length=30,
        null=False,
    )
    age=models.IntegerField(verbose_name='年龄')
    email=models.EmailField(verbose_name='邮箱')
