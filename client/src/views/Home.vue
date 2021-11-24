<template>
  <div class="main-div">
    
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: "Home",
  methods:{
  },
  computed:{
    ...mapState(['movies'])
  },
}
</script>

<style scoped>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
</style>
