<template>
  <div class="hello">
  <!-- <li>{{calendars.full_calendar}}</li> -->

  
  <table class="table table-hover product-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Services</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="key, product in calendars.full_calendar" v-on:click.prevent="onEdit(product)">
        <td>{{product}}</td>
        <td>{{key}}</td>
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
  name: 'hello',
  computed: mapGetters({
    calendars: 'getCalendars'
  })
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
