<template>
  <div>
    <h1>추천 타이틀 페이지 입니다.</h1>
    <input type="text" name="" id="" v-model.trim="titleGet">  
    <button  @click="titleSend">제목 전송</button>
    <div v-if="loding == 2">
     <div> <p>1번  {{ recoGet[1] }}  <button @click="getInfo1" v-if="loding == 2">인포케치</button></p> </div>
      <div v-if="infoChaser == 1">
        <div v-if="tempMovie.id == '0'"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>2번  {{ recoGet[2] }} <button @click="getInfo2" v-if="loding == 2">인포케치</button>  </p></div>
      <div v-if="infoChaser == 2">
          <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
          <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
        </div>
     <div> <p>3번  {{ recoGet[3] }}  <button @click="getInfo3" v-if="loding == 2">인포케치</button> </p></div>
      <div v-if="infoChaser == 3">
          <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
          <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
        </div>
     <div> <p>4번  {{ recoGet[4] }}  <button @click="getInfo4" v-if="loding == 2">인포케치</button> </p></div>
     <div v-if="infoChaser == 4">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>5번  {{ recoGet[5] }}  <button @click="getInfo5" v-if="loding == 2">인포케치</button> </p></div>
     <div v-if="infoChaser == 5">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>6번  {{ recoGet[6] }}  <button @click="getInfo6" v-if="loding == 2">인포케치</button> </p></div>
     <div v-if="infoChaser == 6">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>7번  {{ recoGet[7] }}  <button @click="getInfo7" v-if="loding == 2">인포케치</button> </p></div>
     <div v-if="infoChaser == 7">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>8번  {{ recoGet[8] }} <button @click="getInfo8" v-if="loding == 2">인포케치</button> </p> </div>
     <div v-if="infoChaser == 8">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>
     <div> <p>9번  {{ recoGet[9] }}  <button @click="getInfo9" v-if="loding == 2">인포케치</button> </p></div>
     <div v-if="infoChaser == 9">
        <div v-if="tempMovie.id == 0"> <a :href="tempMovie.urls">이동</a></div>
        <div v-if="tempMovie.id != 0"> {{tempMovie}}</div>
      </div>


    
</div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name : 'RecommendTitle',
  data: function(){
      return {
        titleGet : null,
        recoGet : null,
        loding : 0,
        infoChaser : null,
        tempMovie : null,
      }
    },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    titleSend  : function() {
      const Keyword = {
        titleGet: this.titleGet,
      }
      if (Keyword.titleGet) {
        this.loding = 1
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/title/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          
          if (res.data.state == true) {
            this.recoGet = res.data.Veclist1.title
            console.log(res.data.Veclist1.title[1])
            
          }else{
            alert('검색된 제목이 없습니다! 다른 제목을 넣어주세요~')
          }
          this.loding = 2
        }).catch(err=>{
          console.log(err)
        })
      }
    },
    getInfo1 : function() {
      const movietitles = {
              movieList : this.recoGet[1],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[1]}&section=all`,
              }
              this.infoChaser = 1
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 1
            }
          })
    },
    getInfo2 : function() {
      const movietitles = {
              movieList : this.recoGet[2],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = `https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[2]}&section=all`
              this.infoChaser = 2
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 2
            }
          })
    },
    getInfo3 : function() {
      const movietitles = {
              movieList : this.recoGet[3],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[3]}&section=all`,
              }
              this.infoChaser = 3
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 3
            }
          })
    },
    getInfo4 : function() {
      const movietitles = {
              movieList : this.recoGet[4],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[4]}&section=all`,
              }
              this.infoChaser = 4
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 4
            }
          })
    },
    getInfo5 : function() {
      const movietitles = {
              movieList : this.recoGet[5],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[5]}&section=all`,
              }
              this.infoChaser = 5
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 5
            }
          })
    },
    getInfo6 : function() {
      const movietitles = {
              movieList : this.recoGet[6],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[6]}&section=all`,
              }
              this.infoChaser = 6
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 6
            }
          })
    },
    getInfo7 : function() {
      const movietitles = {
              movieList : this.recoGet[7],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[7]}&section=all`,
              }
              this.infoChaser = 7
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 7
            }
          })
    },
    getInfo8 : function() {
      const movietitles = {
              movieList : this.recoGet[8],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[8]}&section=all`,
              }
              this.infoChaser = 8
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 8
            }
          })
    },
    getInfo9 : function() {
      const movietitles = {
              movieList : this.recoGet[9],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            if (resp.data.title == '영화없음'){
              this.tempMovie = {
                id : 0,
                urls :`https://movie.naver.com/movie/search/result.naver?query=${this.recoGet[9]}&section=all`,
              }
              this.infoChaser = 9
            }else{
            this.tempMovie = resp.data
            this.infoChaser = 9
            }
          })
    },
    getInfo10 : function() {
      const movietitles = {
              movieList : this.recoGet[10],
            }
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/server/recommend/catch/',
              data: movietitles,
              headers: this.setToken()
          }).then(resp=>{
            console.log(resp)
            this.infoChaser = 10
          })
    },

  }
}
</script>

<style>

</style>