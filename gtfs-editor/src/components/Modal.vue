<template>
  <div class="modal">
    <button v-on:click.prevent="onAlert('hello')">Show Changes</button>
    <transition name="modal">
      <div class="modal-mask" v-if="showModal.i" v-on:click.prevent="onClose()">
        <div class="modal-wrapper">
          <div class="modal-container">

            <div class="modal-header">
              <slot name="header">
                <h3>Edits to be committed</h3>
              </slot>
            </div>

            <div class="modal-body">
              <div class="row">
                <div class="col-md-6">
                  <slot name="body">
                    <div v-for="d in showModal.datesOg">
                      <h4 style="text-decoration: underline;">Original</h4>
                      <p>GTFS Date: {{d.d}}</p>
                      <h5 style="margin:0px">Active Calendars:</h5>
                      <p v-for="svc in d.s" style="margin:0px">{{svc}}</p>
                      <h5 style="margin:0px">Inactive Calendars:</h5>
                      <p v-for="svc in d.i" style="margin:0px">{{svc}}</p>
                    </div>
                  </slot>
              </div>
              <div class="col-md-6">
                <slot name="body">
                  <div v-for="d in showModal.datesMod">
                    <h4 style="text-decoration: underline;">Modified</h4>
                    <p>GTFS Date: {{d.d}}</p>
                    <h5 style="margin:0px">Active Calendars:</h5>
                    <p v-for="svc in d.s" style="margin:0px"> {{svc}}</p>
                    <h5 style="margin:0px">Inactive Calendars:</h5>
                    <p v-for="svc in d.i" style="margin:0px">{{svc}}</p>
                  </div>
                </slot>
              </div>

            </div>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="modal-default-button" v-on:click.prevent="onClose()">
                OK
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</div>
</template>

<script>
  export default {
    props: ['showModal'],
    methods: {
      onAlert () {
        this.showModal.i = true
      },
      onClose () {
        this.showModal.i = false
      }
    }
  }
</script>

<style>
  .modal {
    display: inline-block;
  }
  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: table;
    transition: opacity .3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 75%;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;
    overflow: auto;
    max-height:75%;
  }

  .modal-header h3 {
    margin-top: 0;
    color: #42b983;
  }

  .modal-body {
    margin: 20px 0;
  }

  .modal-default-button {
    float: right;
  }

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

 .modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
