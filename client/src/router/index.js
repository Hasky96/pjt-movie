import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '@/views/Movies.vue'
import Home from '@/views/Home.vue'
import Review from '@/views/Review.vue'
import Login from '@/views/Login.vue'
import Recommend from '@/views/Recommend.vue'
import ReviewCreate from '@/views/ReviewCreate.vue'
import ReviewDetail from '@/views/ReviewDetail.vue'
import MovieDetail from '@/views/MovieDetail.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movies/',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/reviews/',
    name: 'Review',
    component: Review
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/recommend/',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/review/',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/review/:reviewId/',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
