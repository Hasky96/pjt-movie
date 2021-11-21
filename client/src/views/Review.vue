<template>
  <div>
    <button @click="$router.push({name: 'ReviewCreate'})">new Review</button>
    <review-list
    :reviews="reviews"
    ></review-list>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import {mapState} from 'vuex'
export default {
  name: "Reviews",
  components:{
    ReviewList,
  },
  methods:{
  },
  computed:{
    ...mapState(['reviews'])
  },
}
</script>

<style>

</style>