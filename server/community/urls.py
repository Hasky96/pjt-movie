from django.urls import path
from . import views

urlpatterns = [
    # 전체리뷰
    path('reviews/', views.all_reviews),
    # 리뷰생성
    path('<int:movie_pk>/new_review/', views.reviews_create),
]
