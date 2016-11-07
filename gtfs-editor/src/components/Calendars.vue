<template>
  <div class="calendars">
  <!-- <span>{{calendars.full_calendar}}</span> -->
  <table class="table table-hover product-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Services</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="svc_id, cal_date in calendars.full_calendar" v-on:click="onEdit(svc_id, cal_date)" v-if="svc_id.length!==0">
        <td>{{cal_date}}</td>
        <td>{{svc_id}}</td>
        <!-- <td><a href="#" v-on:click.prevent.stop="onRemove(product.id)">remove</a></td> -->
      </tr>
      <!-- <tr v-if="!products.length">
        <td colspan="4" class="p-y-3 text-xs-center">
          <strong>You should add some products!</strong>
        </td>
      </tr> -->
    </tbody>
  </table>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  // name: 'calendars',
  computed: mapGetters({
    calendars: 'getCalendars'
  }),
  methods: {
    onEdit (svcId, calDate) {
      var calendarToEdit = {'d': calDate, 's': svcId}
      console.log(calendarToEdit)
      this.$emit('edit', calendarToEdit)
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
