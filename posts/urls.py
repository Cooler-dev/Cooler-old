from django.urls import path
from pywebio.platform.django import webio_view
from . import views

urlpatterns = [
    path('', views.home),
    path('p/<int:id>', views.post)
]
