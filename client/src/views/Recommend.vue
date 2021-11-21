<template>
  <div>
    <h1>추천 페이지 입니다.</h1>
    <recommend-detail></recommend-detail>
  </div>
</template>

<script>
import RecommendDetail from '@/components/RecommendDetail.vue'

export default {
  name: "Recommend",
  components: {
    RecommendDetail,
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