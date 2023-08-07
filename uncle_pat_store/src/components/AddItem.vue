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
      <q-table :rows="tableData" :columns="tableColumns">
        <!-- Add a custom slot for the 'actions' column -->
        <template v-slot:body-cell-actions="{ row }">
          <q-td>
            <q-btn @click="handleEdit(row)" label="Edit" color="primary" />
            <q-btn @click="handleDelete(row)" label="Delete" color="negative" />
          </q-td>
        </template>
      </q-table>
    </q-page>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      itemName: "",
      itemDescription: "",
      itemPrice: 0,
      tableData: [],
      tableColumns: [
        // Define your table columns here
        {
          name: "id",
          required: true,
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        {
          name: "name",
          align: "left",
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          name: "price",
          align: "left",
          label: "Price",
          field: "price",
          sortable: true,
        },
        {
          name: "actions",
          align: "center",
          label: "Actions",
          field: "id", // Use a unique identifier for the item (e.g., 'id')
          format: () => {
            return `
              <q-btn @click="handleEdit(row)" label="Edit" color="primary" />
              <q-btn @click="handleDelete(row)" label="Delete" color="negative" />
            `;
          },
        },

        // Add more columns as needed
      ],
    };
  },
  methods: {
    async fetchItems() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/items/");
        this.tableData = response.data;
      } catch (error) {
        console.error("Error fetching items:", error);
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
        const response = await axios.post(
          "http://127.0.0.1:8000/items/",
          newItem
        );
        this.tableData.push(response.data.item);
      } catch (error) {
        console.error("Error adding item:", error);
      }

      // Clear the input fields after adding the item
      this.itemName = "";
      this.itemDescription = "";
      this.itemPrice = 0;
    },
    async handleEdit(row) {
      try {
        // Implement your logic to handle the edit button click
        // You can use the item data from the 'row' parameter
        console.log("Edit button clicked for item:", row);
      } catch (error) {
        console.error("Error handling edit:", error);
      }
    },
    async handleDelete(row) {
      try {
        // Implement your logic to handle the delete button click
        // You can use the item data from the 'row' parameter
        console.log("Delete button clicked for item:", row);
      } catch (error) {
        console.error("Error handling delete:", error);
      }
    },
  },
  created() {
    this.fetchItems();
  },
};
</script>
