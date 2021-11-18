<template>
  <div>
    <button @click="onC"></button>
  </div>
</template>

<script>
export default {
  name: "Reviews",
  methods:{
    onC(){
      this.$router.push({name: 'Movies'})
    }
  }

}
</script>

<style>

</style>