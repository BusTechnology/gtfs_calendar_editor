import * as actions from './actions'
import * as getters from './getters'

import {
  FETCH_CALENDARS
} from './mutation-types'

// initial state
const initialState = {
  all: []
}

// mutations
const mutations = {
  [FETCH_CALENDARS] (state, calendars) {
    // assign the products that we got from our FETCH_PROUDCTS event to state.all
    state.all = calendars
  }
}

export default {
  state: { ...initialState },
  actions,
  getters,
  mutations
}
