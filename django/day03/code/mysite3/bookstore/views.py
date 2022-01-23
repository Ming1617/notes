from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#file:bookstore/views.py

from . import models

def add_view(request):
    try:
        abook=models.Book.objects.create(
            title='C++',price=35)
        return HttpResponse('添加图书成功！')
    except Exception as err:
        return HttpResponse('添加图书失败！')
