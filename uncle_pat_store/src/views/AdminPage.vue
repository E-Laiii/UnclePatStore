<template>
    <div class="q-pa-md">
        <h1>Admin Page</h1>
        <p>This is where you can change/alter your store items.</p>

        <add-item @add-item="handleAddItem" />
    </div>
    <div>

    </div>
</template>

<script>
// import axios from 'axios';
import AddItem from '../components/AdminMethods.vue';

export default {
  name: 'App',
  components: {
    AddItem
},
  data() {
    return {
      items: [],
    };
  },
  methods: {
    goToAdminPage(){
      this.$router.push({ path: '/admin-page' })
    },
  },

};



</script>