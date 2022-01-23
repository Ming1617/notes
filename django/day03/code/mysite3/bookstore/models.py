from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=30,db_index=True,
                           verbose_name='书名')# varchar(30)
    price=models.DecimalField(decimal_places=2,
                              max_digits=7,
                              null=True,
                              verbose_name='定价') #Decimal(7,2)



