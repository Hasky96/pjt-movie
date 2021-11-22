<template>
  <div>
    <div class="mt-5 container ">
      <img src="..\assets\recommendTitle.png" alt="">
      <hr>
    </div >
      <div v-if="selected == null" class="d-flex justify-content-around">
      <img src="..\assets\keywordsearch.jpg" alt=""  style="width: 25rem; height: 28rem;" class="m-5 box"  @click="keyword">
      <img src="..\assets\titlesearch.jpg" alt=""  style="width: 25rem; height: 28rem;" class="m-5 box"  @click="title">
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
.box {
    border-style: solid;
    border-width: 1px;
    display: block;
    width: 100px;
    height: 100px;
    background-color: #0000FF;
    -webkit-transition:width 2s, height 2s, background-color 2s, -webkit-transform 1s;
    transition:width 2s, height 2s, background-color 2s, transform 1s;
}
.box:hover {
    background-color: #FFCCCC;
    width:200px;
    height:200px;
    -webkit-transform:rotate(360deg);
    transform:rotate(360deg);
}
</style>