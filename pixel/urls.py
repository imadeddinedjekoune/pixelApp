from django.urls import path
from . import views

urlpatterns = [
    path('pixel/', views.pixel_tracker, name='pixel_tracker'),
]