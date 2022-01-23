from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.Author3)
admin.site.register(models.Book3)