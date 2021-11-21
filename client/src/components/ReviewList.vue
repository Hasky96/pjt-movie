<template>
  <div>
    <review-list-item v-for="review in reviews" :key="review.id"
    :review="review"
    >
    </review-list-item>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'


export default {
  components:{
    ReviewListItem,
  },
  props:{
    reviews: Array
  }
}
</script>

<style>

</style>