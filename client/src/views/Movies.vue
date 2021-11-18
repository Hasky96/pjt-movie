<template>
  <div class="movies">
    <div v-if=movie class="moviesChildModal">
      <button @click="exitModal">exit</button>
      <movies-list-item
      :movie="movie"
      ></movies-list-item>
    </div>
    <div>
    <movies-list class="moviesChild"
    @show-detail="showDetail"
    >
    </movies-list>
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList.vue'
import MoviesListItem from '@/components/MoviesListItem.vue'
import {mapState} from 'vuex'


export default {
  name: 'Movies',
  components: {
    MoviesList,
    MoviesListItem
  },
  data : function(){
    return {
      movie:null
    }
  },
  methods:{
    showDetail(movie){
      this.movie = movie
    },
    exitModal(){
      this.movie = null
    }
  },
  computed:{
    ...mapState(['movies'])
  },
}
</script>

<style scoped>
.moviesChild{
  position: absolute;
  z-index: 0;
}

.moviesChildModal{
  position: absolute;
  z-index: 1;
  background: #eee;
}
</style>
