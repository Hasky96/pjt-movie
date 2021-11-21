<template>
  <div id="app">
    <div>
    <!-- Image and text -->
      <b-navbar class="mx-4 justify-content-between" variant="white" type="light">
      <div>
        <router-link to="/">
        <img src="../imgs/film-reel.png" class="d-inline-block" alt="Kitten" width="30px">
         <span class="btn fs-3">MovieFriend</span>
        </router-link>
      </div>
      <div class="text-decoration-none">
        <router-link 
        class="btn fs-5" 
        to="/movies">Movies</router-link>
        <router-link 
        class="btn fs-5" 
        to="/reviews">Reviews</router-link>
        <!-- 추천 시스템 라우터 -->
        <router-link class="btn fs-5" to="/Recommend">Recommend</router-link>
        <!-- 로그인 라우터 -->
        <span v-if="isLogin">
        <router-link class="btn fs-5" @click.native="logout" to="#">Logout</router-link>
        </span>
        <span v-else>
        <router-link class="btn fs-5" to="/login">Login</router-link>
        </span>
        
      </div>
      </b-navbar>
    </div>
    <!--  -->
    <router-view @login="isLogin=true"/>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'App',
  data : function() {
    return{
      isLogin: false
    }
  },
  methods:{
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  beforeCreate: function(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/server/movies/list/',
    }).then(res=>{
      // console.log(res)
      this.$store.dispatch("setMovies", res.data)
    }).catch(err=>{
      console.log(err)
    })
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/server/community/reviews/',
      }).then(res=>{
        console.log(res.data)
        this.$store.dispatch("setReviews", res.data)
      }).catch(err=>{
        console.log(err)
      })
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
