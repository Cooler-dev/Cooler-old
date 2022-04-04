from django.contrib import admin

from meta.models import SiteMeta


class SiteMetaAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


admin.site.register(SiteMeta, SiteMetaAdmin)
