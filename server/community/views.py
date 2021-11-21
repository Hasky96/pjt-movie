from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from community.models import Review, Comment
from movies.models import Movie
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def all_reviews(request):
    reviews = Review.objects.order_by("-pk")
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def reviews_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user= request.user)# 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_detail(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review,user= request.user)# 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def like_review(request,movie_pk,review_pk):
    print(request.user)
    review = get_object_or_404(Review,pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    context = {
        # 'count' : count
    }
    return Response(context, status=status.HTTP_200_OK)
