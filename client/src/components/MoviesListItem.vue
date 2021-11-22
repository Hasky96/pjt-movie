<template>
    <b-col cols="3" class="p-2 movieContainer">
      <div class="poster" @click="showDetail">
        <img :src="movie.poster_path" alt="" height="95%"  width="100%">
        <div class="movieCard">
          <b-card :title="movie.title" :sub-title="movie.release_date" style="height: 80%; overflow:hidden;">
            <b-card-text>
              
            </b-card-text>
            <b-card-text>★ : {{movie.vote_average}}</b-card-text>
          </b-card>
        </div>
      </div>
     
    </b-col >
</template>

<script>
export default {
  name : 'MovieListItem',
  props:{
    movie: Object
  },
  data:function(){
    return{
    }
  },
  methods:{
    showDetail(){
      this.$emit('show-detail', this.movie)
    }
  }
}
</script>

<style scoped>
.movieCard{
  position: absolute;
  height: 80%;
  top: 0px;
  z-index: -1;
  padding-top: 1em;
  padding-right: 1em;
  width: 100%;
}
.movieContainer{
  position: relative;
  padding-bottom: 0px !important;
}
.poster{
  padding: 0px;
  margin: 0px;
  width: 100%;
  height: 100%;
}
.poster>img:hover{
  opacity: 0;
}


</style>