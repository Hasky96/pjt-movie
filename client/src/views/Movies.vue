<template>
  <div class="movies">
    <div>
    <movies-list class="moviesChild"
    :movies ="movies">
    </movies-list>
    </div>
    <div >
      <span v-for="page in pages" :class="{'pagi-active':page==curPage}" :key="page" @click="getPages(page)" class="pagi" >{{page}}</span>
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'Movies',
  components: {
    MoviesList,
  },
  data : function(){
    return {
      movies:null,
      totalPage:null,
      curPage: 1,
      pages : [1, 2, 3, 4, 5]
    }
  },
  methods:{
    reviewPage(movieId){
      this.$router.push({name: 'Review', params: {movieId: movieId}})
    },
    getPages(c){
      this.curPage = c
      let start = c-2
      let end = c+3
      if(c < 1 || c==1 || c==2){
        this.pages = [1, 2, 3, 4, 5]
      }else if(c>this.totalPage || c == this.totalPage|| c.totalPage-1){
        this.pages = [this.totalPage-3, this.totalPage-2, this.totalPage-1, this.totalPage, this.totalPage+1]
      }else{
        this.pages = _.range(start,end)
      }
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/list/${c}/`
      }).then(res=>{
        this.movies = res.data
      }).catch(err=>{
        console.log(err)
      })
    }
  },
  computed:{
  },
  created:function(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/server/movies/list/totalpage/'
    }).then(res=>{
      this.totalPage=res.data.pages
      // console.log(res)
    })
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/list/1/`
      }).then(res=>{
        this.movies = res.data
      })
  }
}
</script>

<style scoped>
.moviesChild{
  z-index: 0;
}
.pagi{
  text-align: center;
  color: #808080;
  font-size: 30px;
  border: #808080 solid 1px;
  background-color: #1b1b1b;
  border-radius: 5px ;
  margin: 5px;
  padding-left: 5px;
  padding-right: 5px;
}
.pagi-active{
  text-align: center;
  color: #1b1b1b;
  font-size: 30px;
  border: #1b1b1b solid 1px;
  background-color: #808080;
  border-radius: 5px ;
  margin: 5px;
  padding-left: 5px;
  padding-right: 5px;
  transform: scale(1.01);
}
</style>
