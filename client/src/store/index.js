import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies : [],
  },
  mutations: {
    SET_MOVIES(state, movies){
      state.movies = movies
    },
  },
  actions: {
    setMovies({commit}, movies){
      commit("SET_MOVIES", movies)
    },
  },
  modules: {
  },
  getters:{
    getMovies(state){
      return state.movies
    }
  }
})
