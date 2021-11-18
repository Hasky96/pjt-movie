<template>
  <div>
    <h1>HOME</h1>
    <div>
      <section @click="move2Movies">Movies</section>
      <section @click="move2Reviews">Reviews</section>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods:{
    move2Movies(){
      this.$router.push('Movies')
    },
    move2Reviews(){
      this.$router.push('Reviews')
    }
  },
}
</script>

<style>

</style>