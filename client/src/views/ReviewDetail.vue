<template>
  <div class="page">
    <header class="hea grayborder">
      <p id="back">리뷰></p>
      <h2 class="my-0 pb-0 reviewTitle">{{review.title}}</h2>
      <div class="py-0 mt-2">
      <span >{{review.user.username}}</span>
      <span >{{review.created_at|moment("from", "now")}}</span>
      </div>
      <p class="my-0">star : {{review.rank}}</p>
    </header>
    <section class="sec">
      <div class="row grayborder">
        <div class="col-1 p-0 ">
          <img :src="movie.poster_path" alt="" width="100%" style="margin: 0px; padding: 0.1em;">
        </div>
        <div class="col">
          <h5 class="fw-bold">{{movie.title}}</h5>
          <span style="font-size: 0.9em">{{movie.release_date}}</span><span style="font-size: 0.9em">star: {{movie.vote_average}}</span>
          <p>{{this.likes}}</p>
          <button @click="like">좋아요</button>
        </div>
        <div class="grayborder reviewContent">
          {{review.content}}
        </div>
      </div>
    </section>
    <footer class="foot grayborder">
      <comment
      :reviewId="review.id"
      :comments="review.comment_set"
      ></comment>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Comment.vue'

export default {
  components: { 
    Comment 
  },
  name: "ReviewDetail",
  data: function(){
    return {
      review: {},
      movie: [],
      likes : null,
    }
  },
  created:function(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/`,
    }).then(res=>{
      this.review = res.data
      this.likes = this.review.like_users.length
      axios({
        method: 'get',
        url : `http://127.0.0.1:8000/server/movies/${res.data.movie}/info/`,
      }).then(res=>{
        // console.log(res.data)
        this.movie = res.data
      }).catch(err=>{
        console.log(err)
      })
    }).catch(err=>{
      console.log(err)
    })
    
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    like : function() { 
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/like/`,
        headers: this.setToken()
        }).then(res=>{
          this.likes = res.data.review
        }).catch(err=>{
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
div{
  margin : 0px
}
*{
  padding: 2px;
  margin: 10px;
  text-align: left;
}
.page{
  height: 100%;
  position: relative;
  padding: 2px;
}
.hea{
  padding: 2px;
  height: 10%;
  position: relative;
}
.sec{
  padding: 2px;
  height: 70%;
  position: relative;
}
.foot{
  padding: 1em;
}
#back{
  margin-bottom: 0px;
  margin-top: 0px;
  color: #03c75a;
  font-size: 0.7rem;
}
#back{
  cursor: pointer;
}
.grayborder{
  border: 1px #eee solid;
}
.reviewTitle{
  height: 3rem;
   overflow: auto;
   font-weight: 900;
   border-bottom: solid #eee 0.5px;
   padding-bottom: 1em;
}
.reviewContent{
  height: 25rem;
  overflow: auto;
  padding-top: 1rem;
  font-size: 1em;
  font-weight: 700;
}
</style>