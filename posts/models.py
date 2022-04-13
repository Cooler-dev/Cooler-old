from django.db import models
from ckeditor.fields import RichTextField



class Post(models.Model):
    name = models.CharField(verbose_name='标题', max_length=100)
    body = RichTextField(verbose_name='正文', max_length=10000, blank=True)

    class Meta(object):
        verbose_name = '文章'
        verbose_name_plural = verbose_name
