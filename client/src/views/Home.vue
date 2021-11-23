<template>
  <div></div>
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
