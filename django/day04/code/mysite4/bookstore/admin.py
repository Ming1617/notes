#file : bookstore/admin.py
from django.contrib import admin

# Register your models here.
from . import models

class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title','pub']
    list_editable = ['price']


admin.site.register(models.Book,BookManager)
class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age']
    list_editable = ['age']

admin.site.register(models.Author,AuthorManager)

class WifeManager(admin.ModelAdmin):
    list_display = ['id','name','author']

admin.site.register(models.Wife,WifeManager)
