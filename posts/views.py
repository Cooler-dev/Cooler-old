from django.shortcuts import render
from posts.models import Post
from meta.models import SiteMeta



def home(request):
    posts = Post.objects.all().order_by('-id')
    meta = SiteMeta.objects.get(id=1)
    context = {
        'posts': posts,
        'meta': meta
    }
    return render(request, 'home.html', context)


def post(request, id):
    meta = SiteMeta.objects.get(id=1)
    post = Post.objects.get(id=id)
    context = {
        'name': post.name,
        'body': post.body,
        'title': meta.title
    }
    return render(request, 'post.html', context)
