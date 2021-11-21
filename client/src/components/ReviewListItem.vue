<template>
  <div @click="$router.push({path:`/review/${review.id}`})">
    {{review}}
  </div>
</template>

<script>
export default {
  props:{
    review : Object
  }
}
</script>

<style>

</style>