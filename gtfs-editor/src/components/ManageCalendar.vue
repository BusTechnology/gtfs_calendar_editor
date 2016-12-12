<template>
  <section>
    <datepicker
      :dateToEdit="dateToEdit"
      v-on:date="onDateSelected"
    ></datepicker>
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
import Datepicker from './DatePicker'

const initialData = () => {
  return {
    calendarToEdit: {
      d: null,
      s: null
    },
    dateToEdit: {
      d: null
    }
  }
}

export default {
  components: {
    Calendars,
    SaveCalendarForm,
    Datepicker
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
      console.log(calendarToEdit)
    },
    onDateSelected (dateToEdit) {
      this.dateToEdit = { ...dateToEdit }
      var month = dateToEdit.d.getMonth() + 1
      if (month < 10) {
        month = '0' + month
      }
      var day = dateToEdit.d.getDate()
      if (day < 10) {
        day = '0' + day
      }
      var gtfsDate = dateToEdit.d.getFullYear() + '' + month + '' + day
      console.log(gtfsDate)
      var active = this.calendars.full_calendar[gtfsDate]
      var inactive = this.calendars.all_service_id.slice(0)
      for (var i = 0; i < active.length; i++) {
        if (inactive.includes(active[i])) {
          var index = inactive.indexOf(active[i])
          inactive.splice(index, 1)
        }
      }
      this.calendarToEdit = {'d': gtfsDate, 's': active, 'i': inactive}
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
