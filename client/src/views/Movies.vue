<template>
  <div class="movies">
    <movie-detail-modal v-if=movie>
      @end-modal="exitModal
      :movie="movie"
    </movie-detail-modal>
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
import {mapState} from 'vuex'
import MovieDetailModal from '@/components/MovieDetailModal.vue'

export default {
  name: 'Movies',
  components: {
    MoviesList,
    MovieDetailModal
  },
  data : function(){
    return {
      movie:null,
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
</style>
