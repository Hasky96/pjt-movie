<template>
  <div style="width:100%;">
    <b-container v-if="movies" style="width:100%;">
      <b-row style="width:100%; ">
        <movies-list-item
        v-for="movie in movies" :key=movie.id
        :movie="movie"
        @show-detail="showDetail"
        >
        </movies-list-item>
      </b-row>
    </b-container>
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