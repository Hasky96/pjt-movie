<template>
  <div class="movies">
    <movies-list
    >
    </movies-list>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList.vue'
import {mapState} from 'vuex'


export default {
  name: 'Movies',
  components: {
    MoviesList,
  },
  data : function(){
    return {
    }
  },
  computed:{
    ...mapState(['movies'])
  },
}
</script>
