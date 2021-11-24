<template>
  <div>
  <div class="main-div" >
    <div class="page-top">
      <div class="page-top-inner-wrap text-center">
        <h2 class="page-title recalltitle">리뷰 리스트</h2>
      </div>
    </div>
    <div class="container recboxs">
    <review-list
    v-model='movieId'
    :reviews="reviews"
    :movieId="movieId"
    ></review-list>
    
    <br>
    <hr>
    <div class="d-flex flex-row justify-content-between">
      <select v-model="movieId" >
        <option value="null">리뷰를 확인 할 영화를 선택해주세요</option>
        <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.title}}</option>
      </select>
      <b-button @click="$router.push({name: 'ReviewCreate'})" >new Review</b-button>
    </div>
    </div>
    </div>
  <footer style="margin-top : 20rem; paddint-bottom : 5rem;">
        <fotter></fotter>
    </footer>
  
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import {mapState} from 'vuex'
import Fotter from '../components/fotter.vue'

export default {
  name: "Reviews",
  components:{
    ReviewList,
    Fotter
  },
  data:function(){
    return{
      movieId : this.$route.params.movieId ?? null,
    }
  }, 
  methods:{
  },
  computed:{
    ...mapState(['movies','reviews']),
  },
  watch:{
    id: function(){
      alert(this.id)
    }
  }
}
</script>

<style>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
.recboxs {
  /* border-radius: 20px; */
  opacity:0.9; 
  margin-top: 3rem;
  padding:2rem;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}

</style>