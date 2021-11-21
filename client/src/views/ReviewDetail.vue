<template>
  <div>{{review}}</div>
</template>

<script>
import axios from 'axios'

export default {
  name: "ReviewDetail",
  data: function(){
    return {
      review: null
    }
  },
  mounted:function(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/`,
    }).then(res=>{
      this.review = res.data
    }).catch(err=>{
      console.log(err)
    })
  }
}
</script>

<style>

</style>