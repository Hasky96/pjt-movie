from django.urls import path
from . import views

urlpatterns = [
    # 전체영화
    path('list/', views.movies),
    # 단일영화
    path('<int:movie_pk>/info/', views.movie_detail),
    # 영화 한줄평
    path('<int:movie_pk>/createComment/', views.comment_create),
    # 한줄평 좋아요
    path('<int:movie_pk>/<int:comment_pk>/like', views.like_comment),

]
