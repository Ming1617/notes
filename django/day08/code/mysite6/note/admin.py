from django.contrib import admin

# Register your models here.

class NoteManager(admin.ModelAdmin):
    list_display = ['user_id','title','user']

from . import models
admin.site.register(models.Note,NoteManager)