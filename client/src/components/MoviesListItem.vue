<template>
    <div @click="showDetail">
      <img :src="movie.poster_path" alt="" height="200px">
      <p> {{movie}}</p>
    </div>
</template>

<script>
export default {
  name : 'MovieListItem',
  props:{
    movie: Object
  },
  methods:{
    showDetail(){
      this.$emit('show-detail', this.movie)
    }
  }
}
</script>

<style>

</style>