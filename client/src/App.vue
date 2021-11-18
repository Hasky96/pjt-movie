<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
import axios from 'axios'

export default {
   beforeCreate: function(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/server/movies/list/',
    }).then(res=>{
      // console.log(res)
      this.$store.dispatch("setMovies", res.data)
    }).catch(err=>{
      console.log(err)
    })
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
