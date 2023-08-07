<template>
  <div>
    <h2>Items in Store</h2>
    <q-list class="q-mb-md">
      <q-item v-for="item in items" :key="item.id">
        <q-item-section>
          <div class="text-h6">{{ item.name }}</div>
          <div class="q-caption text-grey">{{ item.description }}</div>
        </q-item-section>
        <q-item-section side>
          <div class="text-h6 text-weight-medium">${{ item.price }}</div>
        </q-item-section>
        <q-item-section side>
          <q-btn @click="addToCart(item)" color="primary" label="Add to Cart" />
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
export default {
  props: {
    items: Array,
  },
  methods: {
    addToCart(item) {
      // You can implement your logic for adding the item to the cart here
      console.log("Adding item to cart:", item);
    },
  },
};
</script>

<style>
/* You can add custom styles here if needed */
</style>
