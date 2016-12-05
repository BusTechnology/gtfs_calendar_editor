import { http } from 'vue'

import {
  FETCH_CALENDARS,
  SELECT_CALENDAR,
  DESELECT_CALENDAR,
  ACTIVATE_CALENDAR,
  DEACTIVATE_CALENDAR
  // UPDATE_CALENDAR
} from './mutation-types'

export function fetchCalendars ({ commit }) {
  return http.get('calendars')
    .then((response) => commit(FETCH_CALENDARS, response.body))
}

export function updateCalendar ({ commit, state }, calendar) {
  console.log(state.all.full_calendar[calendar.d])
  return http.post('updatecalendars', {calendar: calendar}).then((response) => {
    response.status
  })
}

export function selectSrvToActivate ({ commit, state }, cal) {
  commit(SELECT_CALENDAR, cal)
}

export function activateCalendar ({ commit, state }, cal) {
  commit(ACTIVATE_CALENDAR, cal)
}

export function selectSrvToDeactivate ({ commit, state }, cal) {
  commit(DESELECT_CALENDAR, cal)
}

export function deactivateCalendar ({ commit, state }, cal) {
  commit(DEACTIVATE_CALENDAR, cal)
}
