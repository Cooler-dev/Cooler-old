from django.http import JsonResponse

from api.models import Admin

def home(request):
    date = {
        'name': 'admin'
    }