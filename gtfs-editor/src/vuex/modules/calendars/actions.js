import { http } from 'vue'

import {
  FETCH_CALENDARS
} from './mutation-types'

export function fetchCalendars ({ commit }) {
  return http.get('calendars')
    .then((response) => commit(FETCH_CALENDARS, response.body))
}

