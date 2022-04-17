from meta.models import SiteMeta
from django.http import JsonResponse
from posts.models import Post


def meta(request):
    meta = SiteMeta.objects.get(id=1)
    data = {
        'title': meta.title,
        'author': meta.author
    }
    return JsonResponse(data)
