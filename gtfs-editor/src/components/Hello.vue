<template>
  <div class="hello">
    <section>
      <li>{{calendars.start_date}}</li>
      <li>{{calendars.end_date}}</li>
  </section>
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
