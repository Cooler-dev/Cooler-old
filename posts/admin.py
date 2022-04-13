from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Post, PostAdmin)

admin.site.site_title = "Cooler后台"

admin.site.site_header = "Cooler后台"

admin.site.index_title = "主页"
