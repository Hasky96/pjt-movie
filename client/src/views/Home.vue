<template>
  <div>
    <div class="container">
      <h1>메인 페이지</h1>
      <div>
      <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="3000"
      controls
      fade
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        img-src="https://picsum.photos/1024/480/?image=52"
      ></b-carousel-slide>

      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
        <h1>Hello world!</h1>
      </b-carousel-slide>

      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

      <b-carousel-slide>
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://picsum.photos/1024/480/?image=55"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
          a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
        </p>
      </b-carousel-slide>
    </b-carousel>
  </div>
  <slot-1></slot-1>
  <slot-2></slot-2>
  <slot-3></slot-3>
  <slot-4></slot-4>
  <!-- 하부 슬라이더 들 -->
  
  </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Vue from 'vue'
import 'swiper/dist/css/swiper.css'
import { CarouselPlugin } from 'bootstrap-vue'
import Slot1 from '../components/main/slot1.vue'
import Slot2 from '../components/main/slot2.vue'
import Slot3 from '../components/main/slot3.vue'
import Slot4 from '../components/main/slot4.vue'
Vue.use(CarouselPlugin)
export default {
  name: "Home",
  components: { 
    Slot1,
    Slot2,
    Slot3,
    Slot4,
  },
  data() {
      return {
        slide: 2,
        sliding: null,
        swiperOption: {
          slidesPerView: 2,
          spaceBetween: 30,
          slidesPerGroup: 2,
          loop: true,
          loopFillGroupWithBlank: true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        }
      }
    },
  computed:{
    ...mapState(['movies'])
  },
  methods: {
  onSlideStart(slide) {
    this.sliding = true
    console.log(slide)
  },
  onSlideEnd(slide) {
    this.sliding = false
        console.log(slide)
  }
}
}
</script>

<style scoped>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
</style>
