<template>
  <div id="template">
    <!--이미지-->
    <section class="imgSection">
      <img :src="movie.poster_path" alt="poster" id="imgTag" >
    </section>
    <section class="contentSection">
      <p id="titleTag">{{movie.title}}</p>
      <p id="dateTag">{{movie.release_date}} 개봉</p>
      <p id="rankTag"> <i class="fas fa-star star"/> <span style="filter: contrast(10%);">{{movie.vote_average}}</span></p>
      <p id="contentTag">{{movie.overview}}</p>
    </section>
    <section class="recommendTag">

    </section>
    <section class="community">
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-comment-tab" data-bs-toggle="tab" data-bs-target="#nav-comment" type="button" role="tab" aria-controls="nav-comment" aria-selected="true">Comments</button>
          <button class="nav-link" id="nav-review-tab" data-bs-toggle="tab" data-bs-target="#nav-review" type="button" role="tab" aria-controls="nav-review" aria-selected="false">Reviews</button>
        </div>
      </nav>
        <div class="tab-content" id="nav-tabContent">
          <div class="tab-pane fade show active oneline" id="nav-comment" role="tabpanel" aria-labelledby="nav-comment-tab">
            <movie-comment
            :comments="movie.comment_set"
            >
            </movie-comment>
          </div>
          <div class="tab-pane fade" id="nav-review" role="tabpanel" aria-labelledby="nav-review-tab">
            <review-list class="review"
            :movieId="movie.id"
            ></review-list>
          </div>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import MovieComment from '@/components/MovieComment.vue'
import ReviewList from '@/components/ReviewList.vue'

export default {
  components: { 
    MovieComment,
    ReviewList 
  },
  name: 'MovieDetail',
  data:function(){
    return {
      movie: {}
    }
  },
  created:function(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/movies/${this.$route.params.movieId}/info/`,
    }).then(res=>{
      this.movie = res.data
    }).catch(err=>{
      console.log(err)
    })
    
  }
}
</script>

<style scoped>
#template{
  position: relative;
}
.imgSection{
  height: 40vw;
  margin-top: 0.5em;
  background:black;
}
#imgTag{
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.contentSection{
  /*  */
}
#titleTag{
  font-size: 25px;
  letter-spacing: 0.2px;
  margin: 3vh 10vw;
  margin-bottom: 0px;
  text-align: left;
  color: #808080;
}
#dateTag{
  font-size: 13px;
  letter-spacing: 0.2px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
}
#rankTag{
  font-size: 34px;
  letter-spacing: 0.2px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
}
.star{
  color: gold;
}
#contentTag{
  font-size: 13px;
  letter-spacing: 0.3px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
  height: 200px;
  overflow: auto;
}
#contentTag::-webkit-scrollbar{
  width : 1px;
  background-color:#1b1b1b;
  border: white 1px solid;
}
#contentTag::-webkit-scrollbar-thumb{
  border-radius: 3px;
  background-color:#A5A5A5;
}
#contentTag::-webkit-scrollbar-track{
  background-color:#1b1b1b;
}
.community{
  margin-top: 3em;
  margin-left: 10vw;
  margin-right: 10vw;
  background-color:#1b1b1b;
}
.recommendTag{
   /* 임시 어딘지 보라고 넣어논 border */
   border: white dotted 2px;
  height: 30vw;
  margin-left: 10vw;
  margin-right: 10vw;
}
.review{
  padding: 20px;
  padding-left: 30px;
  padding-right: 30px;
}
</style>
<style>
.active{
  background-color:#808080 !important;
  color:#1b1b1b !important;
}
#nav-comment-tab, #nav-review-tab{
  color: #808080;
  text-align: center  !important;
}
.tab-pane{
  background-color: #1b1b1b !important;
}
</style>
