<template>
  <section>
    <save-calendar-form
      :calendarToEdit="calendarToEdit"
      v-on:activate="onActivate"
      v-on:deactivate="onDeactivate"
      v-on:submit="onSubmit"
    ></save-calendar-form>
    <calendars
      :calendars="calendars"
      v-on:edit="onEditClicked"
    ></calendars>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Calendars from './Calendars'
import SaveCalendarForm from './SaveCalendarForm'

const initialData = () => {
  return {
    calendarToEdit: {
      d: null,
      s: null
    }
  }
}

export default {
  components: {
    Calendars,
    SaveCalendarForm
  },
  data: initialData,
  computed: mapGetters({
    calendars: 'getCalendars'
  }),
  methods: {
    ...mapActions([
      'selectSrvToActivate',
      'activateCalendar',
      'selectSrvToDeactivate',
      'deactivateCalendar',
      'updateCalendar'
    ]),
    onEditClicked (calendarToEdit) {
      this.calendarToEdit = { ...calendarToEdit }
    },
    onActivate (calendar) {
      this.selectSrvToActivate(calendar).then(() => this.activateCalendarInForm())
    },
    onDeactivate (calendar) {
      this.selectSrvToDeactivate(calendar).then(() => this.deactivateCalendarInForm())
    },
    activateCalendarInForm () {
      this.activateCalendar(this.calendarToEdit)
    },
    deactivateCalendarInForm () {
      this.deactivateCalendar(this.calendarToEdit)
    },
    onSubmit (calendar) {
      this.updateCalendar(this.calendarToEdit)
    }
  }
}
</script>
