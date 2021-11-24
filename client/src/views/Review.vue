<template>
  <div >
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
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import {mapState} from 'vuex'

export default {
  name: "Reviews",
  components:{
    ReviewList,
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
.recboxs {
  /* border-radius: 20px; */
  background: #202020;
  opacity:0.9; 
  margin-top: 3rem;
  padding:2rem;
}
</style>