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
import AddItem from '../components/AddItem.vue';

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
    // async handleAddItem(item) {
    //   try {
    //     // const response = await axios.post('http://127.0.0.1:8000/items/', item);
    //     // console.log(item)
    //     // this.items.push(response.data.item);
    //   } catch (error) {
    //     console.error('Error adding item:', error);
    //   }
    // },
  },

};



</script>