from django.db import models


class SiteMeta(models.Model):
    title = models.CharField(default='Cooler站点', verbose_name='站点标题', max_length=10)
    author = models.CharField(verbose_name='作者名称', max_length=10)

    class Meta(object):
        verbose_name = '站点设置'
        verbose_name_plural = verbose_name
