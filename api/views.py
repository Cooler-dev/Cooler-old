from meta.models import SiteMeta
from django.http import JsonResponse
from posts.models import Post
import json

def meta(request):
    meta = SiteMeta.objects.get(id=1)
    data = {
        'title': meta.title,
        'author': meta.author
    }
    data = json.dumps(data)
    return JsonResponse(data)
