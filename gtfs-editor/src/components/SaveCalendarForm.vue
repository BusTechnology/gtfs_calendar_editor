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
          <option v-for="option in calendarToEdit.s" v-bind:value="option">
            {{ option }}
          </option>
        </select>
        <div>Selected Active Service: {{ selected }}</div>
      </div>
      <div class="col-md-4">
        <button type="button" class="btn btn-default" aria-label="Left Align" v-on:click.prevent="onActivate(selected2)" v-if="selected2.length>0">
          Activate
        </button>
        <button type="button" class="btn btn-default" aria-label="Left Align" v-on:click.prevent="onDeactivate(selected)" v-if="selected.length>0">
          Deactivate
        </button>
        <button type="submit" class="btn btn-success" v-on:click.prevent="onSubmit(calendarToEdit)">Submit Changes</button>
        <!-- <button type="submit" class="btn btn-warning">Cancel</button> -->
      </div>
      <div class="form-group col-md-4">
        <label for="price">Inactive Service</label>
        <select v-model="selected2" type="text" class="form-control" id="inactiveService" placeholder="Enter Price" multiple>
          <option v-for="option in calendarToEdit.i" v-bind:value="option">
            {{ option }}
          </option>
        </select>
        <span>Selected Inactive Service: {{ selected2 }}</span>
      </div>
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
      },
      onDeactivate (selected) {
        this.$emit('deactivate', this.selected)
      },
      onSubmit () {
        // if (this.validateForm()) {
        this.$emit('submit', this.calendar)
        // }
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
