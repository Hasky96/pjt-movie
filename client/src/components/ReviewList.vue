<template>
  <div>
    <b-list-group class="px-5 py-3">
      <!-- 제목 -->
      <b-row class="tableHeader fw-bold fs-5">
        <b-col class='myCol' cols="1">작성자</b-col>
        <b-col class='myCol' cols="6">제목</b-col>
        <b-col class='myCol' cols="3">작성일</b-col>
        <b-col class='myCol' cols="2">좋아요</b-col>
      </b-row>
      <b-list-group-item v-if="isSelected">
        <review-list-item  v-for="review in selected" :key="review.id"
        :review="review"
        >
      </review-list-item>
      </b-list-group-item>
      <b-list-group-item v-else>
        <review-list-item v-for="review in reviews" :key="review.id"
        :review="review"
        >
        </review-list-item>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import axios from 'axios'

export default {
  components:{
    ReviewListItem,
  },
  data:function(){
    return{
      selected : null
    }
  },
  methods:{
    getReviews(){
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          console.log(res.data)
          return res.data
        }).catch(err=>{
          console.log(err)
        })
    }
  },
  props:{
    reviews: Array,
    movieId: {
      type: [Number,String],
      default:null,
      required:false
    }
  },
  mounted:function(){
    if(this.movieId=='null' || !this.movieId){
        this.selected=null
      }else{
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          this.selected = res.data
        })
      }
  },
  computed:{
    isSelected:function(){
      // console.log(this.movieId)
      if(this.movieId=='null' || !this.movieId){
        return false
      }else{
        return true
      }
    }
  },
  watch:{
    movieId:function(){
      // console.log(this.movieId)
      if(this.movieId=='null' || !this.movieId){
        this.selected=null
      }else{
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          this.selected = res.data
        })
      }
    }
  }
}

</script>

<style scoped>
.tableHeader{
  border: 2px dotted black;
}
.myCol{
  text-align: center;
} 

</style>