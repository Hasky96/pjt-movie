<template>
    <div>
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
}
</script>

<style>

</style>