<template>
  <section>
    <save-calendar-form
      :calendarToEdit="calendarToEdit"
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
      'saveCalendar'
      // 'deletecalendar'
    ]),
    // onFormSave (calendar) {
    //   this.savecalendar(calendar).then(() => this.resetcalendarInForm())
    // },
    // resetcalendarInForm () {
    //   this.calendarInForm = initialData().calendarInForm
    // },
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
