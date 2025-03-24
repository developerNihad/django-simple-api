from django.urls import path
from .views import demo_endpoint

urlpatterns = [
    path('demo/', demo_endpoint)
]