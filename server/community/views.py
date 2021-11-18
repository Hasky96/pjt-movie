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


#--------- 페이지 정의 -----------#
def community_main(request):
    pass

###------------ 추천시스템 -------------- ###
def movie_recommend(request):
    # Word2Vec 모델 불러오기
    embedding_model = gensim.models.Word2Vec.load('community\word2VecModel')
    print(embedding_model)
    # 시각화 함수 정의
    def w2vvisualization(keyword):
        while True:
            try: 
                labels = []
                tokens = []
                okt = Okt()

                keyword2 = okt.morphs(keyword, stem=True)
                FirstKeyword = keyword2[0]

                VecWords = embedding_model.wv.most_similar(positive=[FirstKeyword], topn=30)
                tokens = []
                labels = []
    #             print(VecWords)
    #             print(embedding_model.get_item()) 
                for i in VecWords :
                    labels.append(i[0])
                    tokens.append(embedding_model.wv[i[0]])

                tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
                new_values = tsne_model.fit_transform(tokens)

                x = []
                y = []

                for value in new_values:
                    x.append(value[0])
                    y.append(value[1])
                # print(x, y)

                a = pd.DataFrame(labels)
                x = pd.DataFrame(x)
                y = pd.DataFrame(y)

                df = pd.concat([a, x, y], axis = 1)
                df.loc[30] = (keyword, 0, 0)
                df.columns  = ['title', 'x', 'y']
                df

                plt.figure(figsize=(16, 16)) 
                plt.rc("font", size = 20)
                for i in range(len(x)-1):
                    # plt.rcParams['font.family'] = 'hanygo250'
                    plt.rcParams['axes.unicode_minus'] = False
                    a = df.loc[[i, 30], :]
                    plt.plot(a.x,a.y, '-D', linewidth = 2)
                    plt.annotate(labels[i],
                                        xy=(df.x[i], df.y[i]),
                                        xytext=(5, 2),
                                        textcoords='offset points',
                                        ha='right',
                                        va='bottom')
                
                
                
                # plt.scatter(df.x[30], df.y[30], s = 1000, marker= '*')
                plt.annotate(keyword,
                                xy=(0, 0),
                                xytext=(10, 5),
                                textcoords='offset points',
                                ha='right',
                                va='bottom')


                plt.show()
                break

            except KeyError: 
                print('다시 입력해주세요. 키워드가 존재하지 않습니다. ')
                pass

    def keyword_check(keyword):
        while True:
            try:
                keyword = okt.morphs(keyword, stem=True)
                FirstKeyword = keyword[0]
                # check embedding result
                VecWords = embedding_model.wv.most_similar(positive=[FirstKeyword], topn=100)
                Veclist1 = []
                for i in range(0,31):
                    Veclist1.append(VecWords[i][0])
            except KeyError: 
                print('다시 입력해주세요. 키워드가 존재하지 않습니다. ')
                pass

    word = input("키워드 입력 : ") #로맨틱 #아련한
    keyword_check(word)



























###------------ 추천시스템 끝 -------------- ###
