<template>
  <b-row @click="$router.push({path:`/review/${review.id}`})" class="review">
    <b-col cols="1">{{review.user.username}}</b-col>
    <b-col cols="6">{{review.title}}</b-col>
    <b-col cols="3">{{review.created_at| moment("from", "now")}}</b-col>
    <b-col cols="2">{{review.like_users|count}}</b-col>
  </b-row>
</template>

<script>
export default {
  props:{
    review : Object
  },
  filters:{
    count: function(arr){
      console.log(arr.length)
      return arr.length
    }
  }
}
</script>

<style scoped>
.review:hover{
  border: #eff solid 1px;
  background: #eee;
  cursor: pointer;
  transform: scale(1.01);
}
</style>