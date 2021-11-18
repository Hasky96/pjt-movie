<template>
  <div>
    <h1>무비리스트</h1>
    <section v-if="movies">
    <movies-list-item
    v-for="movie in movies" :key=movie.id
    :movie="movie"
    @show-detail="showDetail"
    >
    </movies-list-item>
    </section>
    <section v-else>
      <h3>아직 영화정보가 없습니다.</h3>
    </section>
  </div>
</template>

<script>
import MoviesListItem from '@/components/MoviesListItem.vue'
import {mapState} from 'vuex'

export default {
  name: "MovieList",
  components:{
    MoviesListItem,
  },
  data : function(){
    return {
    }
  },
  methods:{
    showDetail(movie){
      this.$emit('show-detail', movie)
    }
  },
  computed:{
    ...mapState(['movies'])
  }
}
</script>

<style>

</style>