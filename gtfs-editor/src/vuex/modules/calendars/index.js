import * as actions from './actions'
import * as getters from './getters'

import {
  FETCH_CALENDARS,
  SELECT_CALENDAR,
  DESELECT_CALENDAR,
  ACTIVATE_CALENDAR,
  DEACTIVATE_CALENDAR
} from './mutation-types'

// initial state
const initialState = {
  all: []
}

// mutations
const mutations = {
  [FETCH_CALENDARS] (state, calendars) {
    // assign the calendars that we got from our FETCH_CALENDARS event to state.all
    state.all = calendars
  },
  [SELECT_CALENDAR] (state, calendar) {
    state.all.svcToActivate = calendar
  },
  [DESELECT_CALENDAR] (state, calendar) {
    state.all.svcToDeactivate = calendar
  },
  [ACTIVATE_CALENDAR] (state, calendar) {
    var activeSrv = calendar.s
    var inactiveSrv = calendar.i
    for (var i = 0; i < state.all.svcToActivate.length; i++) {
      var index = inactiveSrv.indexOf(state.all.svcToActivate[i])
      activeSrv.push(state.all.svcToActivate[i])
      inactiveSrv.splice(index, 1)
    }
    calendar.s = activeSrv
    calendar.i = inactiveSrv
  },
  [DEACTIVATE_CALENDAR] (state, calendar) {
    var activeSrv = calendar.s
    var inactiveSrv = calendar.i

    for (var i = 0; i < state.all.svcToDeactivate.length; i++) {
      var index = activeSrv.indexOf(state.all.svcToDeactivate[i])
      inactiveSrv.push(state.all.svcToActivate[i])
      activeSrv.splice(index, 1)
    }
    calendar.s = activeSrv
    calendar.i = inactiveSrv
  }
}

export default {
  state: { ...initialState },
  actions,
  getters,
  mutations
}
