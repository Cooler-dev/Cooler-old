# Create your models here.
from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    type = "admin"
    class Meta(object):
        verbose_name="管理员信息"
        verbose_name_plural=verbose_name
        db_table='admin'

class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    type = "user"
    class Meta(object):
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
        db_table='users'