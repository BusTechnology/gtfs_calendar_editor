<template>
  <form>
    <div class="form-group" v-bind:class="[{ 'has-danger': formErrors.name }]">
      <label for="calendarName">Calendar Date</label>
      <input type="text" v-model="calendarToEdit.d" class="form-control" id="calendarName" maxlength="32" placeholder="Enter calendar name">
      <div v-if="formErrors.name" class="form-control-feedback">{{formErrors.name}}</div>
    </div>

    <!-- <div class="form-group">
      <label for="calendarDescription">calendar description <small class="text-muted">(optional)</small></label>
      <textarea class="form-control" v-model="calendar.description" id="calendarDescription" rows="3" maxlength="128" placeholder="Enter description"></textarea>
    </div> -->

    <div class="form-group">
      <label for="price">Active Service</label>
      <select type="text" class="form-control" id="activeService" placeholder="Enter Price" multiple>
        <option v-model="calendarToEdit.s" v-for="option in calendarToEdit.s" v-bind:value="option">
        {{ option }}
        </option>
      </select>
      <label for="price">Inactive Service</label>
      <select type="text" class="form-control" id="inactiveService" placeholder="Enter Price" multiple>
        <option v-model="calendarToEdit.i" v-for="option in calendarToEdit.i" v-bind:value="option">
        {{ option }}
        </option>
      </select>
      <!-- <div v-if="formErrors.price" class="form-control-feedback">{{formErrors.price}}</div> -->
    </div>

    <!-- <button type="submit" class="glyphicon glyphicon-chevron-up"> -->
    <!-- <button type="submit" v-on:click.prevent="onSubmit" class="glyphicon glyphicon-star"> -->
      <!-- {{calendar.id ? 'Update' : 'Add'}} calendar -->
    <!-- </button> -->
    <button type="button" class="btn btn-default" aria-label="Left Align">
    Activate
    </button>
    <button type="button" class="btn btn-default" aria-label="Left Align">
    Deactivate
    </button>
    <!-- <button type="submit" v-if="calendar.id" v-on:click.prevent="onCancel" class="btn btn-secondary">Cancel</button> -->
    <button type="submit" class="btn btn-success">Submit</button>
    <button type="submit" class="btn btn-warning">Cancel</button>
  </form>
</template>

<script>
export default {
  props: ['calendarToEdit'],
  data () {
    return {
      formErrors: {}
    }
  }
  // watch: {
  //   ['calendarToEdit']() {
  //     this.formErrors = {};
  //   }
  // },
  // methods: {
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
</style>
