from django.http import JsonResponse


def author(request):
    date = {
        'name': 'demo'
    }
    return JsonResponse(date)
