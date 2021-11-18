from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from community.models import Review
from movies.models import Movie
from .serializers import ReviewListSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def all_reviews(request):
    reviews = Review.objects.order_by("-pk")
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([AllowAny])
def reviews_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)# user= request.user
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#------- 추천시스템 import -------#
import pandas as pd
import tweepy
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)
import gensim
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from gensim.models import Word2Vec
from konlpy.tag import Okt # 옛날 Twitter 클래스
okt = Okt()
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Word2Vec 모델 불러오기
embedding_model = gensim.models.Word2Vec.load('community\word2VecModel')



#--------- 페이지 정의 -----------#
def community_main(request):
    pass

###------------ 추천시스템 -------------- ###
@api_view(['POST'])
@permission_classes([AllowAny])
def movie_recommend(request):
    # 키워드 check (입력 키워드가 이상하면 다시)
    def keyword_check(keyword):
        try:
            keyword = okt.morphs(keyword, stem=True)
            FirstKeyword = keyword[0]
            # check embedding result
            VecWords = embedding_model.wv.most_similar(positive=[FirstKeyword], topn=100)
            Veclist1 = []
            for i in range(0,31):
                Veclist1.append(VecWords[i][0])
            context = {
                'state' : True,
                'Veclist1' : Veclist1[:10],
                'first_keyword' : keyword
            }
            return context
        except KeyError: 
            # keyError 값을 return 해줘야 하는데??
            # 리턴값이 XX 이면 ALTER 을 발생?
            context = {
                'state' : False
            }
            return context
    # 이때 키워드는 request 에 담겨서 넘어와야 한다.
    word  = request.POST.get('name')#로맨틱 #아련한
    print(word)
    context = keyword_check(word)
    return Response(context, status=status.HTTP_200_OK)




















###------------ 추천시스템 끝 -------------- ###
