<template>
    <div class="q-pa-md">
        <h1>Welcome to the Uncle Pat Store</h1>
        <p>This is where all the best goods are sold</p>

        <item-list :items="items" />

    </div>
</template>

<script>
import axios from 'axios';
import ItemList from '../components/ItemList.vue';


export default {
  name: 'App',
  components: {
    ItemList,
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
    async fetchItems() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/items/');
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    },
  },
  created() {
    this.fetchItems();
  },
};

</script>
