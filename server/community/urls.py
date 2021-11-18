from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_main),
    path('recommend/', views.movie_recommend),
]
