from django.urls import path
from .pages.machine import MachinePage

urlpatterns = [
    path("", MachinePage.index, name='home'),
]