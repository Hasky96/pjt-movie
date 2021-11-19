<template>
  <div>
    <h1>추천 페이지 입니다.</h1>
  </div>
</template>

<script>
export default {
  name: "Recommend",
  methods:{
    onC(){
      this.$router.push({name: 'Recommend'})
    }
  }

}
</script>

<style>

</style>