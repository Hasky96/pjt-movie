<template>
    <b-col cols="3" class="p-2 movieContainer" >
      <div class="poster-movie" @click="$router.push({path:`/movie/${movieId}/`})">
        <div class="imgDiv">
          <img class="imgTag" :class="{'imgTag-hover':ishover}" :src="movie.poster_path" alt="" width="100%">
        </div>
        <div class="movieContent" @mouseover="ishover=true" @mouseleave="ishover=false">
          <h4 class="fw-bold">{{movie.title}}</h4>
          <p>{{movie.release_date}}</p>
          <p class="vote"><i class="fas fa-star starTag"/> {{movie.vote_average}}</p>
        </div>
      </div>
    </b-col >
</template>

<script>
export default {
  name : 'MovieListItem',
  props:{
    movie: Object,
    movieId:Number
  },
  data(){
    return{
      ishover: false
    }
  },
  methods:{
  }
}
</script>

<style scoped>
.movieContent{
  padding: 30px;
  text-align: left;
  position: absolute;
  width: 100%;
  height: 100%;
  color: white;
  opacity: 0%;
  z-index: 2;
}
.movieContent:hover{
  transition-duration: 1s;
  opacity: 100%;
}
.movieContainer{
  position: relative;
  padding-bottom: 0px !important;
}
.poster-movie{
  position: relative;
  background-color: black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 0px;
  margin: 0px;
  overflow: hidden;
  vertical-align: middle;
}
.imgDiv{
  max-height: 100%;
}
.imgTag-hover{
  opacity: 20%;
  transition-duration: 0.5s;
}
.imgTag{
  display: block;
  margin: auto;
}
.starTag{
  color: gold;
  font-size: 30px;
}
.vote{
  font-size: 30px;
}

</style>