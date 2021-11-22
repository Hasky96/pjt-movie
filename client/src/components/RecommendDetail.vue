<template>
  <div style="background : white;">
    <h1>키워드 추천 페이지 입니다!</h1>
    <!-- 키워드 입력  -->
    <input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 0 " @keyup.enter="onB">
    <input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 1 " @keyup.enter="onC">
    <input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 2 " @keyup.enter="onD">
    <b-button v-if="tryNum == 0" @click="onB" variant="outline-primary">첫번째 전송</b-button>
    <b-button v-if="tryNum == 1" @click="onC" variant="outline-primary">두번째 전송</b-button>
    <b-button v-if="tryNum == 2" @click="onD" variant="outline-primary">세번째 전송</b-button>
    <b-button v-if="tryNum == 4" @click="reset">리셋</b-button>

    <!-- if 로 첫번째, 두번째 ,세번째 키워드 넣을 수 있도록 하고, 이후에는 연관 키워드 선택하기 or 그냥 키워드 입력하기로 할 수 있도록 -->
    <transition name="fade">
      <div v-if="tryNum == 1">
        <h2>첫번째 키워드 {{ firstKeyword }}에 대한 연관 키워드 입니다.</h2>
        <div v-for="vec in firstData" :key="vec.id">
            <p>{{vec}}</p>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="tryNum == 2">
        <h2>두번째 키워드 {{ secoundKeyword }}에 대한 연관 키워드 입니다.</h2>
        <p v-for="vec in secoundData" :key="vec.id">
            <a href="" >{{vec}}</a>
          </p>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="tryNum == 3">
        <div v-if="loding == 0">
        <h2>선택하신 키워드는 다음과 같습니다.</h2>
        <p>첫번째 키워드 : {{firstKeyword}}</p>
        <p>두번째 키워드 : {{secoundKeyword}}</p>
        <p>세번째 키워드 : {{thirdKeyword}}</p>
        <button v-if="tryNum == 3" @click="getMovie">키워드 전송!</button>
        <b-button  @click="reset">리셋</b-button>
        </div>
      </div>
    </transition>
    <img src="..\assets\CMCLoading.gif" alt="" v-if="loding == 1">
    <transition name="fade" >
    <div v-if="tryNum == 4" class="container">
      <div v-if="loding == 2" class="">
        <hr>
        
          <div v-for="movieEl in movieList" v-bind:key="movieEl">
            <b-container class="bv-example-row text-center" >
              <b-row class=" justify-content-md-center text-center" >
                <b-col cols="1" class="d-flex align-items-center text-center">{{movieEl[0]}}</b-col>
                <b-col cols="4" class="d-flex align-items-center text-center">{{movieEl[1]}}</b-col>
                <b-col cols="5" class="d-flex align-items-center text-center">{{movieEl[2]}}</b-col>
                <b-col cols="1" class="d-flex align-items-center text-center">
                  <a v-if="movieEl[0] != '순번'" :href="movieEl[3]">  <b-button variant="outline-primary">이동</b-button></a>
                    <p v-if="movieEl[0] == '순번'">{{movieEl[3]}}</p>
                  </b-col>
              </b-row>
            </b-container>
            <hr>
          </div>
        
      </div>
    </div>
  </transition>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name :'RecommendKeyword',
  data: function(){
      return {
        tryNum : 0,
        firstData: null,
        firstKeyword : null,
        inputKeyword : null,
        secoundKeyword: null,
        secoundData : null,
        thirdData : null,
        thirdKeyword : null,
        movieData : null,
        reviewData : null,
        loding :0 ,
        number : 1,
        movieList : null,
        keywordTitle : null,
        show: true
      }
    },
  methods :{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    onB : function(){
      
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          if (res.data.state == true){
          this.loding = 1
          console.log(res)
          this.firstData = res.data.Veclist1
          this.firstKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    onC : function(){
      
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          this.loding = 1 
          if (res.data.state == true){
          console.log(res)
          this.secoundData = res.data.Veclist1
          this.secoundKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    onD : function(){
      
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        this.loding = 1
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
         if (res.data.state == true){
          console.log(res)
          this.thirdData = res.data.Veclist1
          this.thirdKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    getMovie : function(){
      this.loding = 1
      const keyWordData = {
        firstData : this.firstData,
        firstKeyword : this.firstKeyword,
        secoundData: this.secoundData,
        secoundKeyword : this.secoundKeyword,
        thirdData : this.thirdData,
        thirdKeyword : this.thirdKeyword,
      }
      axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/server/recommend/movie/',
      data: keyWordData,
      headers: this.setToken()
      }).then(res=>{
        // console.log(res) 
        console.log(res)
        this.movieData = res.data.movie_list
        const movie_list = [['순번' ,'제목', '사용자 리뷰','영화링크']]

        var step;
        for (step = 0; step < 20; step++) {
          movie_list.push([this.number,res.data.movie_list.영화명[step], res.data.movie_list.리뷰[step],`https://movie.naver.com/movie/search/result.naver?query=${res.data.movie_list.영화명[step]}&section=all`])
          this.number += 1
        } 
        this.movieList = movie_list
        console.log(movie_list)
        this.tryNum += 1
        this.loding = 2
        this.number = 1
      }).catch(err=>{
        console.log(err)
        this.loding = 2
      })
      
    },
    reset : function() {
      this.loding = 0
      this.tryNum = 0
    } 
    }
    
  }
  
  
</script>

<style>
.fade-enter {
  opacity: 0;
}
.fade-enter-active{
  transition: opacity 1s ease-in;
  }
.fade-leave-active {
  transition: opacity 0.2s ease-out;
}
.fade-leave-to {
   opacity: 0;

}

</style>