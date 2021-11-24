<template>
<div>
    <div class="container-sm" v-if="movies">
      <div class="row" style="">
        <movies-list-item 
        v-for="movie in movies" :key=movie.id
        :movie="movie.fields"
        :movieId="movie.pk"
        >
        </movies-list-item>
      </div>
    </div>
    <section v-else>
      <h3>아직 영화정보가 없습니다.</h3>
    </section>
  </div>

</template>

<script>
import MoviesListItem from '@/components/MoviesListItem.vue'

export default {
  name: "MovieList",
  components:{
    MoviesListItem,
  },
  data : function(){
    return {
    }
  },
  props:{
    movies : Array
  },
  methods:{
  },
}
</script>

<style>
</style>