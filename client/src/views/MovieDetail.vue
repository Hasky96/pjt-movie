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
      <!-- 추천 시스 -->
      <div >
        <br>
      <h2 style="margin-top : 2rem;">추천 영화</h2>
      <div class="container" style="margin-top : 2rem">
           <swiper class="swiper" :options="swiperOption">
             <!-- div로 감싸고, 크기 조절하면 될 듯 -->
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[0]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[0] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[1]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[1] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[2]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[2] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[3]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[3] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[4]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[4] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[5]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[5] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[6]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[6] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[7]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[7] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[8]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[8] }}</p> <br></div></swiper-slide>
            <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[9]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[9] }}</p> <br></div></swiper-slide>
            <div class="swiper-pagination" slot="pagination"></div>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
        </div>
        </div>
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
            <movie-comment></movie-comment>
          </div>
          <div class="tab-pane fade" id="nav-review" role="tabpanel" aria-labelledby="nav-review-tab">
            
          </div>
        </div>
    </section>
{{movie}}
  </div>
</template>

<script>
import axios from 'axios'
import MovieComment from '@/components/MovieComment.vue'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

export default {
  components: { 
    MovieComment,
    swiper,
    swiperSlide,
  },
  name: 'MovieDetail',
  data:function(){
    return {
      movie: {},
      movieList : null,
      number : 1,
    swiperOption: {
          slidesPerView: 5,
          spaceBetween: 30,
          slidesPerGroup: 5,
          loop: true,
          loopFillGroupWithBlank: true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        }
      
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
  },
  created:function(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/movies/${this.$route.params.movieId}/info/`,
    }).then(res=>{
      this.movie = res.data
      axios({
              method: 'get',
              url: `http://127.0.0.1:8000/server/recommend/${res.data.id}/detail/`,
              headers: this.setToken(),
              }).then(res=>{
                this.movieList = res.data
              }).catch(err=>{
                console.log(err)
              })
    }).catch(err=>{
      console.log(err)
    })
    
  },
}
</script>

<style scoped>
#template{
  position: relative;
}
.imgSection{
  height: 40vw;
  margin-top: 3em;
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
}
.recommendTag{
   /* 임시 어딘지 보라고 넣어논 border */
  background: #1b1b1b;
  height: 30vw;
  margin-left: 10vw;
  margin-right: 10vw;
}
.swiper-button-next,
.swiper-button-prev, 
.swiper-container-rtl .swiper-button-prev,
.swiper-container-rtl .swiper-button-next{
    fill: #000;
}
.recplat {
  background: #808080;
}


</style>
<style>
.active{
  background-color:#808080 !important;
  color:#1b1b1b !important;
}
#nav-comment-tab, #nav-review-tab{
  color: #808080;;
}

</style>
