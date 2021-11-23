<template>
  <div id="d">
    <h1 class="text-light">Welcome Home</h1>
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
</style>