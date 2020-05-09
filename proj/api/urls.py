from django.urls import path
from .views import Image

urlpatterns = [
    path('images/', Image.as_view()),
]
