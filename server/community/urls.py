from django.urls import path
from . import views

urlpatterns = [
    # 전체리뷰
    path('reviews/', views.all_reviews),
    # 리뷰생성
    path('<int:movie_pk>/new_review/', views.reviews_create),
    # 리뷰의 detail
    path('review/<int:review_pk>/', views.reviews_detail),
    # 리뷰의 like
    path('review/<int:review_pk>/like/', views.like_review),
    # 리뷰의 comment
    path('review/<int:review_pk>/createComment/', views.comment_create),
    # 특정영화 ID의 리뷰만 주세요
    path('movie/<int:movie_id>/reviews/', views.review_by_movieID)

]
