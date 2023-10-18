from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    country=models.CharField(max_length=20)

class footballplayerAdmin(admin.ModelAdmin):
    list_display=['name','salary','age','email','country']
