import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies : [],
    reviews: [],
  },
  mutations: {
    SET_MOVIES(state, movies){
      state.movies = movies
    },
    SET_REVIEWS(state, reviews){
      state.reviews = reviews
    },
  },
  actions: {
    setMovies({commit}, movies){
      commit("SET_MOVIES", movies)
    },
    setReviews({commit}, reviews){
      commit("SET_REVIEWS", reviews)
    },
  },
  modules: {
  },
  getters:{
    getMovies(state){
      return state.movies
    },
    getReviews(state){
      return state.reviews
    }
  }
})
