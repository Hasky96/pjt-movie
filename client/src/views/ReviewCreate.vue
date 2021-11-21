<template>
  <div>
    <label for="reviewTitle">title : </label>
    <input v-model="title" name="reviewTitle" type="text">
    <div>
      <div class="rate">
        <input v-model="rankString" type="radio" id="star5" name="rate" value=5 />
        <label  for="star5" title="text">5 stars</label>
        <input v-model="rankString" type="radio" id="star4" name="rate" value="4" />
        <label for="star4" title="text">4 stars</label>
        <input v-model="rankString" type="radio" id="star3" name="rate" value="3" checked/>
        <label for="star3" title="text">3 stars</label>
        <input v-model="rankString" type="radio" id="star2" name="rate" value="2" />
        <label for="star2" title="text">2 stars</label>
        <input v-model="rankString" type="radio" id="star1" name="rate" value="1" />
        <label for="star1" title="text">1 star</label>
      </div>
    </div>
    <label for="reviewContent">content : </label>
    <textarea v-model="content" 
    style="resize:none"
    name="reviewContent" type="textarea" cols="50" rows="10"/>
    <button @click="create">작성하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreate',
  data:function(){
    return {
      movieId: 1,
      rankString:"",
      title: null,
      content: null,
    }
  },
  computed:{
    rankInt : function(){
      return parseInt(this.rankString)
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    create(){
      console.log(this.rankInt)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/server/community/${this.movieId}/new_review/`,
        data: {
          title : this.title,
          content : this.content,
          rank: this.rankInt,
        },
        headers: this.setToken()
      }).then(()=>{
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/server/community/reviews/',
        }).then(res=>{
          console.log(res.data)
          this.$store.dispatch("setReviews", res.data)
        }).catch(err=>{
          console.log(err)
        })
        this.$router.push({name:'Review'})
      }).catch(err=>{
        console.log(err)
      })
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      //pass
    } else {
      alert("로그인 해주세요!")
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
.rate {
  text-align: center;
  display: inline-block;
  margin: 0 auto;
  /* float: left; */
  height: 46px;
  padding: 0 10px;
}
.rate:not(:checked) > input {
  position:absolute;
  top:-9999px;
}
.rate:not(:checked) > label {
  float:right;
  width:1em;
  overflow:hidden;
  white-space:nowrap;
  cursor:pointer;
  font-size:30px;
  color:#ccc;
}
.rate:not(:checked) > label:before {
  content: '★ ';
}
.rate > input:checked ~ label {
  color: gold;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
  color: gold;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
  color: gold;
}


</style>