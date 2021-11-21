from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from movies.serializers import CommentSerializer, MovieSerializer
from rest_framework import status
from .models import Movie, Comment
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movies(request):
    movies_list = Movie.objects.all()
    serializer = MovieSerializer(movies_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 한줄평 만들기
@api_view(["POST"])
@permission_classes([AllowAny])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)# user= request.user
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 한줄평 좋아요
@api_view(["POST"])
@permission_classes([AllowAny])
def like_comment(request,movie_pk,comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    # count = review.like_users
    context = {
        # 'count' : count
    }
    return Response(context, status=status.HTTP_200_OK)