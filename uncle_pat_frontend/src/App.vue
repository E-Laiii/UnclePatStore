<template>
  <img alt="Vue logo" src="./assets/logo1.png">
  <div id="app">
    <h1>Basic Store</h1>
    <item-list :items="items" />
    <add-item @add-item="handleAddItem" />
  </div>
</template>

<script>
import axios from 'axios';
import ItemList from './components/ItemList.vue';
import AddItem from './components/AddItem.vue';

export default {
  name: 'App',
  components: {
    ItemList,
    AddItem,
  },
  data() {
    return {
      items: [],
    };
  },
  methods: {
    async fetchItems() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/items/');
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    },
    async handleAddItem(item) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/items/', item);
        this.items.push(response.data.item);
      } catch (error) {
        console.error('Error adding item:', error);
      }
    },
  },
  created() {
    this.fetchItems();
  },
};
</script>

<style>
/* Add any custom styles here */
</style>
