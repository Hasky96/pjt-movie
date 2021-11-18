<template>
  <div>
    <label for="username">ID : </label>
    <input v-model="credential.username" name="username" type="text">
    <label for="password">PW : </label>
    <input v-model="credential.password" @keyup.enter="login" name="password" type="password">
    <button @click="login">LOGIN</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Login",
  data: function(){
    return {
      credential:{
        username: null,
        password: null
      }
    }
  },
  methods:{
    login(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/accounts/api-token-auth/',
        data: this.credential
      }).then(res=>{
        const jwt = res.data.token
        localStorage.setItem('jwt', jwt)
        this.$emit('login')
        this.$router.push({ name: 'Movies' })
      })
    }
  }
}
</script>

<style>

</style>