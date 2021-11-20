<template>
  <div>
    <h1>추천 디데틸 페이지 입니다.</h1>
    <!-- 키워드 입력  -->
    <input type="text" name="" id="" v-model.trim="inputKeyword">
    <button @click="onB">첫번째 전송</button>
    <h2>{{ firstKeyword }}에 대한 연관 키워드 입니다.</h2>
    <p v-for="vec in firstData" :key="vec.id">
        <a href="">{{vec}}</a>
      </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name :'RecommendDetail',
  data: function(){
      return {
        firstData: null,
        firstKeyword : null,
        inputKeyword : null,
      }
    },
  methods :{
    onB : function(){
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      console.log(Keyword)
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword
        }).then(res=>{
          // console.log(res)
          console.log(res)
          this.firstData = res.data.Veclist1
          this.firstKeyword = res.data.first_keyword
        }).catch(err=>{
          console.log(err)
        })
      }
    },
    // sendB : function() {
    //   const Keyword = {
    //     inputKeyword: this.inputKeyword,
    //   }
    //   console.log(Keyword)
    //   if (Keyword.inputKeyword) {
    //     axios({
    //     method: 'post',
    //     url: 'http://127.0.0.1:8000/server/recommend/',
    //     data: Keyword
    //     }).then(res=>{
    //       // console.log(res)
    //       console.log(res)
    //       this.firstData = res.data.Veclist1
    //       this.firstKeyword = res.data.first_keyword
    //     }).catch(err=>{
    //       console.log(err)
    //     })
    //   }
    }
  }
  
</script>

<style>

</style>