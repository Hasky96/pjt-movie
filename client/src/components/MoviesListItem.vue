<template>
    <div class="col-sm-3 p-2 movieContainer" >
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
    </div >
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
  position: absolute;
  text-align: left;
  color: white;
  opacity: 0%;
  width: 100%;
  height: 100%;
  z-index: 2;
  top: 0px;
  padding: 30px;
}
.movieContent:hover{
  transition-duration: 1s;
  opacity: 100%;
}
.movieContainer{
  height: 100%;
}
.poster-movie{
  position: relative;
  background-color: black;
  align-items: center;
  height: 100%;
  padding: 0px;
  margin: 0px;
  overflow: hidden;
  vertical-align: middle;
}
.imgDiv{
  height: 100%;
}
.imgTag-hover{
  opacity: 20%;
  transition-duration: 0.5s;
}
.imgTag{
  height: 80%;
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