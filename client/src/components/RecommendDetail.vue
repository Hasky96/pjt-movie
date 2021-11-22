<template>
  <div>
    <h1>추천 디데일 페이지 입니다.</h1>
    <!-- 키워드 입력  -->
    <input type="text" name="" id="" v-model.trim="inputKeyword">
    <button v-if="tryNum == 0" @click="onB">첫번째 전송</button>
    <button v-if="tryNum == 1" @click="onC">두번째 전송</button>
    <button v-if="tryNum == 2" @click="onD">세번째 전송</button>


    <!-- if 로 첫번째, 두번째 ,세번째 키워드 넣을 수 있도록 하고, 이후에는 연관 키워드 선택하기 or 그냥 키워드 입력하기로 할 수 있도록 -->
    <div v-if="tryNum == 1">
      <h2>{{ firstKeyword }}에 대한 연관 키워드 입니다.</h2>
      <p v-for="vec in firstData" :key="vec.id">
          <button >{{vec}}</button>
        </p>
    </div>
    <div v-if="tryNum == 2">
      <h2>{{ secoundKeyword }}에 대한 연관 키워드 입니다.</h2>
      <p v-for="vec in secoundData" :key="vec.id">
          <a href="" >{{vec}}</a>
        </p>
    </div>
    <div v-if="tryNum == 3">
      <h2>선택하신 키워드는 다음과 같습니다.</h2>
      <p>첫번째 키워드 : {{firstKeyword}}</p>
      <p>두번째 키워드 : {{secoundKeyword}}</p>
      <p>세번째 키워드 : {{thirdKeyword}}</p>
      <button v-if="tryNum == 3" @click="getMovie">키워드 전송!</button>
    </div>
    <div v-if="tryNum == 4">
      <h2>선택하신 키워드는 다음과 같습니다.</h2>
      <p>첫번째 키워드 : {{firstKeyword}}</p>
      <p>두번째 키워드 : {{secoundKeyword}}</p>
      <p>세번째 키워드 : {{thirdKeyword}}</p>
      <p v-for="moviel in movieData" :key="moviel.id">
      {{moviel}} 
        </p>
    </div>
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
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          // console.log(res)
          console.log(res)
          this.firstData = res.data.Veclist1
          this.firstKeyword = res.data.first_keyword
          this.tryNum += 1
        }).catch(err=>{
          console.log(err)
        })
      }
    },
    onC : function(){
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword
        }).then(res=>{
          // console.log(res)
          console.log(res)
          this.secoundData = res.data.Veclist1
          this.secoundKeyword = res.data.first_keyword
          this.tryNum += 1
        }).catch(err=>{
          console.log(err)
        })
      }
    },
    onD : function(){
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword
        }).then(res=>{
          // console.log(res)
          console.log(res)
          this.thirdData = res.data.Veclist1
          this.thirdKeyword = res.data.first_keyword
          this.tryNum += 1
        }).catch(err=>{
          console.log(err)
        })
      }
    },
    getMovie : function(){
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
      data: keyWordData
      }).then(res=>{
        // console.log(res)
        console.log(res)
        this.movieData = res.data.movie_list

        this.tryNum += 1
      }).catch(err=>{
        console.log(err)
      })
      
    },    
    }
  }
  
</script>

<style>

</style>