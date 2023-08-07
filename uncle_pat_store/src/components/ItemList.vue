<template>
    <div>
      <h2>Items in Store</h2>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }} - ${{ item.price }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      items: Array,
    },
  };
  </script>

<style>

ul {
  list-style: none;
}
</style>
  