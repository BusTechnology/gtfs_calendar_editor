<template>
  <section>
    <datepicker
      :dateToEdit="dateToEdit"
      v-on:date="onDateSelected"
    ></datepicker>
    <modal
      :showModal="showModal"
    ></modal>
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
import Modal from './Modal'

const initialData = () => {
  return {
    calendarToEdit: {
      d: null,
      s: null
    },
    dateToEdit: {
      d: null
    },
    showModal: {
      i: false,
      datesOg: [],
      datesMod: []
    }
  }
}

export default {
  components: {
    Calendars,
    SaveCalendarForm,
    Datepicker,
    Modal
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
      this.showModal.datesOg.indexOf(this.calendarToEdit) === -1 ? this.showModal.datesOg.push(JSON.parse(JSON.stringify(this.calendarToEdit))) : console.log('This item already exists')
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
      var active = this.calendars.full_calendar[gtfsDate]
      var inactive = this.calendars.all_service_id.slice(0)
      for (var i = 0; i < active.length; i++) {
        if (inactive.includes(active[i])) {
          var index = inactive.indexOf(active[i])
          inactive.splice(index, 1)
        }
      }
      this.calendarToEdit = {'d': gtfsDate, 's': active, 'i': inactive}
      this.showModal.datesOg.indexOf(this.calendarToEdit) === -1 ? this.showModal.datesOg.push(JSON.parse(JSON.stringify(this.calendarToEdit))) : console.log('This item already exists')
    },
    onActivate (calendar) {
      this.selectSrvToActivate(calendar).then(() => this.activateCalendarInForm())
    },
    onDeactivate (calendar) {
      this.selectSrvToDeactivate(calendar).then(() => this.deactivateCalendarInForm())
    },
    activateCalendarInForm () {
      this.showModal.datesMod.indexOf(this.calendarToEdit) === -1 ? this.showModal.datesMod.push(this.calendarToEdit) : console.log('This item already exists')
      this.activateCalendar(this.calendarToEdit)
    },
    deactivateCalendarInForm () {
      this.showModal.datesMod.indexOf(this.calendarToEdit) === -1 ? this.showModal.datesMod.push(this.calendarToEdit) : console.log('This item already exists')
      this.deactivateCalendar(this.calendarToEdit)
    },
    onSubmit (calendar) {
      this.updateCalendar(this.calendarToEdit)
    }
  }
}
</script>
