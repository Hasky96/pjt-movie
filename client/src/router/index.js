import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '@/views/Movies.vue'
import Home from '@/views/Home.vue'
import Review from '@/views/Review.vue'
import Login from '@/views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
