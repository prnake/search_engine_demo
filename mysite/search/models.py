from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-c_time']
        verbose_name = "用户"
        verbose_name_plural = "用户"

class HotSpot(models.Model):
    word = models.CharField(max_length=100,unique=True)
    count = models.IntegerField(default=0)
    class Meta:
        ordering = ['-count']
        verbose_name = "热搜"
        verbose_name_plural = "热搜"
    def __str__(self):
        return self.word
