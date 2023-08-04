<template>
    <div>
      <h2>Add Item</h2>
      <form @submit.prevent="addItem">
        <input v-model="newItem.name" type="text" placeholder="Item Name" required>
        <input v-model="newItem.price" type="number" placeholder="Item Price" required>
        <button type="submit">Add Item</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newItem: {
          name: '',
          price: null,
        },
      };
    },
    methods: {
      addItem() {
        this.$emit('add-item', { ...this.newItem });
        this.newItem = { name: '', price: null };
      },
    },
  };
  </script>
  