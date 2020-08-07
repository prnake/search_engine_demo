from django.contrib import admin
from . import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','password','c_time','ip']

class HotSpotAdmin(admin.ModelAdmin):
    list_display = ['word', 'count']

admin.site.register(models.User,UserAdmin)
admin.site.register(models.HotSpot,HotSpotAdmin)
