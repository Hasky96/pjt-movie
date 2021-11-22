<template>
  <div>
    <select v-model="movieId">
      <option value="null">영화를 선택해주세요</option>
      <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.title}}</option>
    </select>
    <button @click="$router.push({name: 'ReviewCreate'})">new Review</button>
    <review-list
    v-model='movieId'
    :reviews="reviews"
    :movieId="movieId"
    ></review-list>
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

</style>