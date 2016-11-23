<template>
  <form>
    <div class="form-group col-md-12" v-bind:class="[{ 'has-danger': formErrors.name }]">
      <label for="calendarName">Calendar Date</label>
      <input type="text" v-model="calendarToEdit.d" class="form-control" id="calendarName" maxlength="32" placeholder="Enter calendar name">
      <div v-if="formErrors.name" class="form-control-feedback">{{formErrors.name}}</div>
    </div>
    <div class="row">
      <div class="form-group col-md-4">
        <label for="price">Active Service</label>
        <select v-model="selected" type="text" class="form-control" id="activeService" placeholder="Enter Price" multiple>
          <!-- <option v-model="calendarToEdit.s" v-for="option in calendarToEdit.s" v-bind:value="option"> -->
          <option v-for="option in calendarToEdit.s" v-bind:value="option">
            {{ option }}
          </option>
        </select>
        <div>Selected Active Service: {{ selected }}</div>
      </div>
      <div class="col-md-4">
        <button type="button" class="btn btn-default" aria-label="Left Align" v-on:click.prevent="onActivate(selected2)">
          Activate
        </button>
        <button type="button" class="btn btn-default" aria-label="Left Align" v-on:click.prevent="onDeactivate(selected)">
          Deactivate
        </button>
        <!-- <button type="submit" v-if="calendar.id" v-on:click.prevent="onCancel" class="btn btn-secondary">Cancel</button> -->
        <button type="submit" class="btn btn-success">Submit</button>
        <button type="submit" class="btn btn-warning">Cancel</button>
      </div>
      <div class="form-group col-md-4">
        <label for="price">Inactive Service</label>
        <select v-model="selected2" type="text" class="form-control" id="inactiveService" placeholder="Enter Price" multiple>
          <!-- <option v-model="calendarToEdit.i" v-for="option in calendarToEdit.i" v-bind:value="option"> -->
          <option v-for="option in calendarToEdit.i" v-bind:value="option">
            {{ option }}
          </option>
        </select>
        <span>Selected Inactive Service: {{ selected2 }}</span>
        <!-- <div v-if="formErrors.price" class="form-control-feedback">{{formErrors.price}}</div> -->
      </div>
      <!-- <button type="submit" class="glyphicon glyphicon-chevron-up"> -->
      <!-- <button type="submit" v-on:click.prevent="onSubmit" class="glyphicon glyphicon-star"> -->
      <!-- {{calendar.id ? 'Update' : 'Add'}} calendar -->
      <!-- </button> -->

    </div>

    
  </form>
</template>

<script>
  export default {
    props: ['calendarToEdit'],
    data () {
      return {
        formErrors: {},
        selected: [],
        selected2: []
      }
    },
  // watch: {
  //   ['calendarToEdit']() {
  //     this.formErrors = {};
  //   }
  // },
    methods: {
      onActivate (selected2) {
        this.$emit('activate', this.selected2)
      // this.$emit('select', this.selected2)
      // var active = calendarToEdit.s.slice(0) // clone list of serviceId's
      // var inactive = calendarToEdit.i.slice(0) // clone list of serviceId's
      // for (var i = 0; i < inactive.length; i++) {
      //   for (var j = 0; j < selected2.length; j++) {
      //     if (selected2[j] === inactive[i]) {
      //       console.log(selected2[j])
      //       var svcId = inactive[i]
      //       // var svc_id = calendarToEdit.i.splice(i, 1)
      //       active.push(svcId)
      //       console.log(active)
      //     }
      //   }
      // }
      // console.log(calendarToEdit.i)
      },
      onDeactivate (selected) {
        this.$emit('deactivate', this.selected)
      }
    }
  //   validateForm() {
  //     const errors = {};

  //     if (!this.calendar.name) {
  //       errors.name = 'Name is required'
  //     }

  //     if (!this.calendar.price) {
  //       errors.price = 'Price is required'
  //     }

  //     this.formErrors = errors;

  //     return Object.keys(errors).length === 0 ;
  //   },
  //   onCancel() {
  //     this.formErrors = {}

  //     this.$emit('cancel');
  //   },
  //   onSubmit() {
  //     if (this.validateForm()) {
  //       this.$emit('submit', this.calendar);
  //     }
  //   }
  // }
}
</script>

<style scoped>
  form {
    margin-bottom: 24px;
  }
  #activeService {
    height: 300px;
  }
  #inactiveService {
    height: 300px;
  }
</style>
