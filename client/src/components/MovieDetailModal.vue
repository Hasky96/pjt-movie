<template>
    <div>
    <div class="movie">
        <img class="movieImg" :src="movie.poster_path" alt="" height="100%">
        <div class="movieInfo p-3">
        <h3 class="fw-bold">{{movie.title}}</h3> <br>
        <strong>개봉일 : {{movie.release_date}}</strong>
        <br><br>
        <strong>★ :{{movie.vote_average}}({{movie.vote_count}})</strong>
        </div>
    </div>
    <strong class="p-3 overview"> {{movie.overview}}</strong>
    </div>
</template>
<script>
export default {
    name : 'MovieDetailModal',
    props: {
        movie : Object
    },
    methods:{
        endModal(){
            this.$emit('end-modal')
        }
    }
}
</script>
<style scoped>
*{
    padding: 0;
    margin: 0;
}
.movie{
    width: 100%;
}
.movieImg{
    width: 40%;
    top: 0%;
}
.movieInfo{
    vertical-align:middle;
    display: inline-block;
    width: 60%
}
.overview{
    overflow: auto;
    height: 20em;
    font-style: bold;
    }
</style>