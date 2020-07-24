from django.urls import path
from . import views

# Urls Patterns

urlpatterns = [
    path('contact', views.contact, name='contact'),
]
