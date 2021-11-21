from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
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
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
# Word2Vec 모델 불러오기
embedding_model = gensim.models.Word2Vec.load('recommend\word2VecModel')
###------------ 추천시스템 -------------- ###

# 키워드 송출 시스템
@api_view(['POST'])
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
                'state' : False,
                'Veclist1' : '다른 키워드를 넣어주세요!',
            }
            return context
    # 이때 키워드는 request 에 담겨서 넘어와야 한다.
    word  = request.data.get('inputKeyword')#로맨틱 #아련한
    print(type(request.data.get('list')))
    print(3, word)
    context = keyword_check(word)
    return Response(context, status=status.HTTP_200_OK)

# 추천영화 전송 시스템
@api_view(['POST'])
def show_recommend_movie(request):
    FirstKeyword  = request.data.get('firstKeyword')# 첫번째 키워드
    print(FirstKeyword)
    SecondKeyword  = request.data.get('secoundKeyword')# 두번째 키워드
    ThirdKeyword  = request.data.get('thirdKeyword')# 세번째 키워드
    print(SecondKeyword,ThirdKeyword)
    # list_num  = request.# 리스트
    Veclist1  = request.data.get('firstData')# 리스트
    Veclist2  = request.data.get('secoundData')# 리스트
    Veclist3  =request.data.get('thirdData')# 리스트
    # 벡터 가중치 설정
    print(Veclist1,Veclist2,Veclist3)
    myVec = [FirstKeyword]*3+Veclist1+[SecondKeyword]*2+Veclist2[:5]+[ThirdKeyword] + Veclist3[:5]
    # print(Veclist1)
    # 테이블 불러오기
    mymyCut = pd.read_csv("recommend\리뷰코사인을위한데이터테이블3.csv")
    
    # 코사인 유사도 확인
    mysent=""
    for i in myVec:
        mysent += "".join(i)
        mysent += " "
    mydf = pd.Series(['입력',mysent,mysent], index=["영화명","리뷰","word"])
    mymyCut = mymyCut.append(mydf, ignore_index=True)
    mymyCut.iloc[-1,:]
    # TFIDF 설정
    Tfidf = TfidfVectorizer() 
    Tfidf_matrix = Tfidf.fit_transform(mymyCut['word'])

    cosine_sim = linear_kernel(Tfidf_matrix, Tfidf_matrix)

    def getRecommendation1(cosine_sim= cosine_sim):
        # idx = indices[title]
        simScores = list(enumerate(cosine_sim[-1])) #코사인유사도
        # simScores : 튜플 (인덱스,코사인유사도)
        simScores = sorted(simScores, key=lambda x: x[1] ,reverse=True)
        # 코사인유사도 기준 내림차순 정렬된 튜플중 자기 제외하고 20개 뽑음
        simScores = simScores[1:21]
        # 상위 20개 영화의 인덱스값 저장
        movieidx = [i[0] for i in simScores]
        RecMovielist = mymyCut.iloc[movieidx] 
        return RecMovielist[['영화명','리뷰']]
    
    movie_list = getRecommendation1()
    context = {
        'movie_list' : movie_list
    }
    return Response(context, status=status.HTTP_200_OK)

