from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_recommend),
    path('movie/', views.show_recommend_movie),
]
