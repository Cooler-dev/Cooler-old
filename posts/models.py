from django.db import models


class Post(models.Model):
    name = models.CharField(verbose_name='标题', max_length=100)
    abstract = models.TextField(verbose_name='摘要', max_length=10000, blank=True)
    body = models.TextField(verbose_name='正文', max_length=10000, blank=True)

    class Meta(object):
        verbose_name = '文章'
        verbose_name_plural = verbose_name
