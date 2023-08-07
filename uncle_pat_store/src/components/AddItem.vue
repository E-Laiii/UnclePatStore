<template>
    <div>
      <h2>Add Item</h2>
      <form @submit.prevent="addItem">
        <label>
        Name:
        <input type="text" v-model="itemName" />
      </label>
      <label>
        Description:
        <input type="text" v-model="itemDescription" />
      </label>
      <label>
        Price:
        <input type="number" v-model="itemPrice" />
      </label>
      <button type="submit">Add Item</button>
      </form>

          <!-- Your table to display existing items goes here -->
    <q-page>
      <q-table :rows="tableData" :columns="tableColumns" />
    </q-page>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        itemName: '',
      itemDescription: '',
      itemPrice: 0,
      tableData: [],
      tableColumns: [
        // Define your table columns here
        { name: 'id', required: true, label: 'ID', align: 'left', field: 'id', sortable: true },
        { name: 'name', align: 'left', label: 'Name', field: 'name', sortable: true },
        { name: 'price', align: 'left', label: 'Price', field: 'price', sortable: true },
        // Add more columns as needed
      ],
      };
    },
    methods: {
    async fetchItems() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/items/');
        this.tableData = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    },
    async addItem() {
      const newItem = {
        id: this.id,
        name: this.itemName,
        description: this.itemDescription,
        price: this.itemPrice,
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/items/', newItem);
        this.tableData.push(response.data.item);
      } catch (error) {
        console.error('Error adding item:', error);
      }

      // Clear the input fields after adding the item
      this.itemName = '';
      this.itemDescription = '';
      this.itemPrice = 0;
    },
  },
  created() {
    this.fetchItems();
  },
  };
  </script>
  