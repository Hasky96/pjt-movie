<template>
  <div>
  <div class="comment" v-for="comment in comments" :key="comment.id">
    <span class="user">{{comment.user.username}}</span>
    <span class="line mx-2">-</span>
    <span class="commenttext">{{comment.content}}</span>
  </div>
  </div>
</template>

<script>
export default {

  props:{
    reviewId: Number,
    comments: Array
  },
  data:function(){
    return {
    }
  },
}
</script>

<style scoped>
.comment{
  padding-top: 0.5em;
  padding-bottom: 0.5em;
  width : 100%;
  margin: 0px;
}
.user{
  padding: 0.5em;
  border: #eee solid 1px;
  border-radius: 0.7em;
}
.commenttext{
  padding: 0.5em;
  border: #eee solid 1px;
  border-radius: 0.7em;
}
.line{
  font-size: 1.5em;
}
</style>