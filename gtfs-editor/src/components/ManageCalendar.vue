<template>
  <section>
    <save-calendar-form
      :calendarToEdit="calendarToEdit"
      v-on:activate="onActivate"
      v-on:deactivate="onDeactivate"
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
      'saveCalendar',
      'saveCalendar2',
      'saveCalendar3',
      'saveCalendar4'
      // 'deletecalendar'
    ]),
    onActivate (calendar) {
      this.saveCalendar(calendar).then(() => this.resetCalendarInForm())
    },
    onDeactivate (calendar) {
      this.saveCalendar3(calendar).then(() => this.resetCalendarInForm2())
    },
    resetCalendarInForm () {
      this.saveCalendar2(this.calendarToEdit)
    },
    resetCalendarInForm2 () {
      this.saveCalendar4(this.calendarToEdit)
    },
    onEditClicked (calendarToEdit) {
      this.calendarToEdit = { ...calendarToEdit }
    }
    // onRemoveClicked(calendar) {
      // this.deletecalendar(calendar).then(() => {
        // if (calendar.id === this.calendarInForm.id) {
          // this.resetcalendarInForm();
        // }
      // });
    // }
  }
}
</script>
