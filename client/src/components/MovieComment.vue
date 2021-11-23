<template>
  <div class="container row px-5">
    <div class="newDiv row g-0">
      <span class="col-10"><input type="text"></span><span class="col-2"><button >작성</button></span>
    </div>
    <article class="comment" v-for="comment in comments" :key="comment.id" >
      <i class="fas fa-star star"/> <span class="rank">{{comment.rank}}</span>
      <span class="content">{{comment.content}}</span>
    </article>
  </div>
</template>

<script>
export default {
  props:{
    comments: Array
  }
}
</script>

<style scoped>
.container{
  align-content: center;
  text-align: left;
  margin: 0px;
  padding: 0px;
  background-color: #1b1b1b;
  width: 100%;
  max-width: 100%;
}
.newDiv{
  margin: 0px;
  margin-top: 10px;
}
.newDiv > span > input{
  background: #1b1b1b;
  border: 1px #808080 solid;
  border-radius: 5px;
  height: 40px;
  font-size: 20px;
  color: #808080;
  width: 100%;
  padding-right: 0px;
}
.newDiv > span > button{
  background: #1b1b1b;
  color: #808080;
  border: 1px #808080 solid;
  border-radius: 5px;
  height: 40px;
  width: 100%;
}
.star{
  font-size: 20px;
  color: gold;
}
.comment{
  text-align: left;
  padding: 10px;
  background-color: #1b1b1b;
  color: #808080;
}
.rank{
  font-size: 20px;
}
.content{
  margin-left: 20px;
}
</style>