from django.shortcuts import render
from posts.models import Post
from meta.models import SiteMeta
from django.http import HttpResponse


def home(request,):
    posts = Post.objects.all()
    meta = SiteMeta.objects.all()
    context = {
        'posts': posts,
        'meta': meta,
    }
    return render(request, 'home.html', context)


def post(request, id):
    meta = SiteMeta.objects.all()
    post = Post.objects.get(id=id)
    context = {
        'name': post.name,
        'body': post.body
    }
    return render(request, post.html, context)
