<template>
  <div class="movies">
    <movies-list class="moviesChild"
    @show-detail="setDetail"
    >
    </movies-list>
    <b-modal id=modal-movie ok-title="후기보기!" ok-only @ok="reviewPage(movie.id)">
      <div>
      <movie-detail-modal
      :movie=movie
      >
      </movie-detail-modal>
      </div>
    </b-modal>
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
    MovieDetailModal,
  },
  data : function(){
    return {
      movie:null,
    }
  },
  methods:{
    reviewPage(movieId){
      this.$router.push({name: 'Review', params: {movieId: movieId}})
    },
    setDetail(movie){
      this.movie = movie
      this.$bvModal.show('modal-movie')
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
