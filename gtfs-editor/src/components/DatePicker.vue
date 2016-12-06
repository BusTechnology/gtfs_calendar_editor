<template>
  <div id="app">
  <h1>Datepicker</h1>
  <div class="example">
    <h3>Events</h3>
    <datepicker name="eventtest"></datepicker>
    <div class="settings">
      <h5>Output</h5>
      <div class="form-group">
        <p>{{ eventMsg }}</p>
      </div>
    </div>
  </div>
  <div class="example">
    <h3>Inline datepicker</h3>
    <datepicker :inline="true"></datepicker>
  </div>
  </div>
</template>

<script>
  import Datepicker from 'vuejs-datepicker'

  var state = {
    date1: new Date()
  }

  export default {
    // props: ['format'],
    components: {
      Datepicker
    },
    data () {
      return {
        format: 'd MMMM yyyy',
        disabled: {},
        eventMsg: null,
        state: state
      }
    },
    ready () {
      this.$on('datepicker.eventtest', (val) => {
        this.eventMsg = 'Date picked! ' + new Date(val.value)
      })
    }
  }
</script>

<style>
  body {
    font-family: 'Helvetica Neue Light', Helvetica, sans-serif;
    padding: 1em 2em 2em;
  }
  input, select {
    padding: .75em .5em;
    font-size: 100%;
    border: 1px solid #ccc;
    width: 100%;
  }

  select {
    height: 2.5em;
  }

  .example {
    background: #f2f2f2;
    border: 1px solid #ddd;
    padding: 0em 1em 1em;
    margin-bottom: 2em;
  }

  code,
  pre {
    margin: 1em 0;
    padding: 1em;
    border: 1px solid #bbb;
    display: block;
    background: #ddd;
    border-radius: 3px;
  }

  .settings {
    margin: 2em 0;
    /*padding: 0 1.5em 1.5em*/
    border-top : 1px solid #bbb;
    background: #eee;
  }

  h5 {
    font-size:100%;
    padding: 0;
  }

  .form-group {
    margin-bottom: 1em;
  }

  .form-group label {
    font-size: 80%;
    display: block;
  }

</style>