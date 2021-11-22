<template>
  <div>
    <div class="mt-5 container  ">
      <img src="..\assets\recommendTitle.png" alt="">
      <hr>
    </div>
    
      <b-button @click="keyword" variant="outline-primary">키워드 추천</b-button>
      <b-button @click="title" variant="outline-primary">제목 추천</b-button>

    <div v-if="selected == 1">
      <recommend-detail></recommend-detail>
    </div>
    <div v-if="selected == 2">
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

</style>