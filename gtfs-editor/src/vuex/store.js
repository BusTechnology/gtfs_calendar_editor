import Vue from 'vue'
import Vuex from 'vuex'

import calendars from './modules/calendars'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    calendars
  },
  strict: debug
})
