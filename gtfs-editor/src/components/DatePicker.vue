<template>
  <div id="app">
  <h1>GTFS Calendar Editor</h1>
    <div class="example">
      <h3>Choose date to edit:</h3>
      <datepicker v-model="eventMsg" :inline="true" :format="format"></datepicker>
        <!-- <a name="calForm" href="#calform"> -->
        <!-- <button type="button" class="btn btn-default" aria-label="Left Align">Select Calendar   -->
        <a name="calForm" href="#calform"><button type="button" class="btn btn-default" aria-label="Left Align" v-on:click.prevent="onDate(eventMsg)">Select Calendar  
        </button>
        <!-- </a> -->
    </div>
  </div>
</template>

<script>
  import Datepicker from 'vuejs-datepicker'

  var state = {
    date1: new Date()
  }

  export default {
    components: {
      Datepicker
    },
    methods: {
      onDate: function (val) {
        var dateToEdit = {'d': val}
        this.$emit('date', dateToEdit)
      }
    },
    data () {
      return {
        // dateToEdit: null,
        format: 'yyyyMMdd',
        disabled: {},
        eventMsg: null,
        state: state
      }
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