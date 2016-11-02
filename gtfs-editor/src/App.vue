<template>
  <div>
    <main class="container">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Calendars from './components/Calendars'

export default {
  components: {
    Calendars
  },

  created () {
    this.$store.dispatch('fetchCalendars')
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
