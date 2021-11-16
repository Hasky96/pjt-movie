from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_main)
]
