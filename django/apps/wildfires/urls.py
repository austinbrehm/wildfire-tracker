from django.urls import path
from . import views

urlpatterns = [
    path('', views.wildfires_list, name='wildfires'),
]