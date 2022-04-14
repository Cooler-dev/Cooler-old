from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('p/<int:id>', views.post)
]
