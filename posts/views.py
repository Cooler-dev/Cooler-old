from django.shortcuts import render
from posts.models import Post
from meta.models import SiteMeta


def home(request):
    posts=Post.objects.all()
    meta=SiteMeta.objects.all()

    return render(request, 'home.html', {'meta': meta, 'posts': posts})
