<template>
    <div>
     <img :src="movie.poster_path" alt="" height="200px">
      <p> {{movie}}</p>
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
<style>
    
</style>