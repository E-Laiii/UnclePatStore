<template>
    <div class="q-pa-md">
        <h1>Welcome to the Uncle Pat Store</h1>
        <img
        alt="Uncle Pat logo"
        src="../assets/logo.png"
        style="width: 200px; height: 200px; display: block; margin: auto;"
      />
        <p class="text-center">Best goods only.</p>
        
        <!-- Your table to display existing items -->
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
    // Fetching items
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
