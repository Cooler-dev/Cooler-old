from django.http import HttpResponse
from meta.models import SiteMeta


def home(request):
    MetaTitle = SiteMeta.objects.all()
    title = MetaTitle.get['title']
    return HttpResponse(title)
