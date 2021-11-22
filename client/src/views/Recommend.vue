<template>
  <div>
    <div class="page-top">
      <div class="page-top-inner-wrap">
        <h2 class="page-title">추천 시스템</h2>
      </div>
    </div>
  <div class="mt-5 container ">
      
      <hr>
    </div >
    <!-- style="width: 25rem; height: 28rem;" -->
      <div v-if="selected == null" class="d-flex justify-content-around">
        <div class="recbox" @click="keyword">
          <img src="..\assets\keyword.png" alt="" class="recpic">
          <h2 class="rectitle">키워드 추천</h2>
          <div class="reccontent">
            <h4> 3만개의 리뷰를 바탕으로 키워드에 최적화 된 영화를 추천합니다.
            </h4>
          </div>
        </div>
        <div class="recbox" @click="title">
          <img src="..\assets\keyword.png" alt="" class="recpic">
          <h2 class="rectitle">타이틀 추천</h2>
          <div class="reccontent">
            <h4> 영화 제목의 코사인 유사도를 바탕으로 가장 비슷한 영화를 추천합니다.
            </h4>
          </div>
        </div>
    </div>
    <div v-if="selected == 1">
      <div  class="d-flex justify-content-center">
      <b-button @click="keyword" class="m-3 mt-0 mb-2">키워드 추천</b-button>
      <b-button @click="title" class="m-3 mt-0 mb-2">타이틀 추천</b-button>
      </div>
      <recommend-detail></recommend-detail>
    </div>
    <div v-if="selected == 2">
      <div class="d-flex justify-content-center">
      <b-button @click="keyword" class="m-3 mt-0 mb-2">키워드 추천</b-button>
      <b-button @click="title" class="m-3 mt-0 mb-2">타이틀 추천</b-button>

      </div>
      <recommend-title></recommend-title>
    </div>
  </div>
</template>

<script>
import RecommendDetail from '@/components/RecommendDetail.vue'
import RecommendTitle from '@/components/RecommendTitle.vue'

export default {
  name: "Recommend",
  components: {
    RecommendDetail,
    RecommendTitle
  },
  data: function(){
      return {
        tryNum : 0,
        selected: null
      }
  },
  methods :{
    keyword : function() {
      this.selected = 1
    },
    title : function() {
      this.selected = 2
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      //pass
    } else {
      alert("로그인 해주세요!")
      this.$router.push({name: 'Login'})
    }
  }

}
</script>

<style>
.recpic {
  width: 18rem; 
  height: 18rem;
}
.reccontent {
  margin: auto;
  color: white;
}
.rectitle {
  margin-bottom: 2rem;
  color: white;
}
.recbox {
  border: solid;
  border-color: white;
  width: 25rem; 
  height: 28rem;
  background: #252525;
  -webkit-transition:width 2s, height 2s, background-color 2s, -webkit-transform 2s;
  transition:width 2s, height 2s, background-color 2s, transform 2s;
}
.page-top-inner-wrap {
    position: relative;
    max-width: 1240px;
    margin: 0px auto;
    text-align: left;
}
.page-title {
    font-size: 24px;
    line-height: 36px;
    color: rgb(255, 255, 255);
    font-weight: 400;
}
.page-top {
  background: #252525;
  padding: 40px 0px;
  text-align: left;
  margin: 0 auto;

}

</style>