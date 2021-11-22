<template>
  <div>
    <label for="username">ID : </label>
    <input v-model="credential.username" name="username" type="text">
    <label for="password">PW : </label>
    <input v-model="credential.password" @keyup.enter="login" name="password" type="password">
    <button @click="login">LOGIN</button>
    <b-button v-b-modal.modal-signup>회원가입</b-button>
    <b-modal id=modal-signup ok-title="signup" @ok="signup">
      <div>
          <label for="username">ID : </label>
          <input v-model="credential.username" name="username" type="text">
          <label for="password">PW : </label>
          <input v-model="credential.password" name="password" type="password">
          <label for="passwordConfirmation">PW : </label>
          <input v-model="credential.passwordConfirmation" @keyup.enter="signup" name="passwordConfirmation" type="password">
      </div>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
  components: { 
    
  },
  name: "Login",
  data: function(){
    return {
      credential:{
        username: null,
        password: null,
        passwordConfirmation: null,
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
        this.$session.start()
        this.$session.set('jwt', jwt)
        Vue.http.headers.common['Authorization'] = `JWT ${jwt}`
        this.$emit('login')
        this.$router.push({ name: 'Movies' })
      })
    },
    signup(){
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/server/accounts/signup/',
                data: this.credential
            }).then((res)=>{
                console.log(res)
                alert(`${res.data.username} 가입성공!`)
            }).catch(err=>{
                console.log(err)
            })
    },
  },
  created: function (){
    if (localStorage.getItem('jwt')) {
      this.$router.push({name: 'Movies'})
    }
  }
}
</script>

<style>

</style>