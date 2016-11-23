import { http } from 'vue'

import {
  FETCH_CALENDARS,
  SELECT_CALENDAR,
  DESELECT_CALENDAR,
  ACTIVATE_CALENDAR,
  DEACTIVATE_CALENDAR
} from './mutation-types'

export function fetchCalendars ({ commit }) {
  return http.get('calendars')
    .then((response) => commit(FETCH_CALENDARS, response.body))
}

export function updateCalendar ({ commit }, calendar) {
  return http.put(`calendars/${calendar}`, calendar)
    .then((response) => commit(SELECT_CALENDAR, response.body.data))
}

export function saveCalendar ({ commit, state }, cal) {
  commit(SELECT_CALENDAR, cal)
}

export function saveCalendar2 ({ commit, state }, cal) {
  commit(ACTIVATE_CALENDAR, cal)
}

export function saveCalendar3 ({ commit, state }, cal) {
  commit(DESELECT_CALENDAR, cal)
}

export function saveCalendar4 ({ commit, state }, cal) {
  commit(DEACTIVATE_CALENDAR, cal)
}
