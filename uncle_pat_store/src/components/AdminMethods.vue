<template>
  <div>
    <h2>Add Item</h2>
    <form @submit.prevent="addItem">
      <label>
        Name:
        <input type="text" v-model="itemName" required />
      </label>
      <label>
        Description:
        <input type="text" v-model="itemDescription" required />
      </label>
      <label>
        Price:
        <input type="number" v-model="itemPrice" step="0.01" required min="0" />
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

      <!-- Dialog for updating the row -->
      <q-dialog v-model="dialogVisible">
        <q-card>
          <q-card-section>
            <q-input v-model="editedItem.name" label="Name" />
            <q-input v-model="editedItem.description" label="Description" />
            <q-input v-model="editedItem.price" label="Price" type="number" />
          </q-card-section>

          <q-card-actions align="right">
            <q-btn @click="cancelEdit" label="Cancel" />
            <q-btn @click="saveEdit" label="Save" color="primary" />
          </q-card-actions>
        </q-card>
      </q-dialog>

      <q-dialog v-model="deleteConfirmationVisible">
        <q-card>
          <q-card-section>
            <p>Are you sure you want to delete this item?</p>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn @click="cancelDelete" label="Cancel" />
            <q-btn @click="confirmDelete" label="Delete" color="negative" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-page>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dialogVisible: false,
      itemName: "",
      itemDescription: "",
      itemPrice: 0,
      deleteConfirmationVisible: false,
      itemToDelete: null,
      editedItem: {
        id: null,
        name: "",
        description: "",
        price: 0,
      },
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
          name: "description",
          align: "left",
          label: "Description",
          field: "description",
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
          align: "left",
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
      // Validate the inputs before submitting
      if (!this.itemName || !this.itemDescription || this.itemPrice <= 0) {
        alert(
          "Please fill in all the required fields and provide a valid price."
        );
        return;
      }

      const newItem = {
        name: this.itemName,
        description: this.itemDescription,
        price: this.itemPrice,
      };

      try {
        // Save the item to the backend
        await axios.post(
          "http://127.0.0.1:8000/items/",
          newItem
        );

        // Fetch the updated data from the backend after item creation
        const updatedItemsResponse = await axios.get(
          "http://127.0.0.1:8000/items/"
        );
        this.tableData = updatedItemsResponse.data;
      } catch (error) {
        console.error("Error adding item:", error);
      }

      // Clear the input fields after adding the item
      this.itemName = "";
      this.itemDescription = "";
      this.itemPrice = 0;
    },
    async handleEdit(row) {
      // Set the editedItem with the values of the selected row
      this.editedItem = { ...row };
      this.dialogVisible = true; // Show the dialog
    },
    cancelEdit() {
      this.dialogVisible = false; // Hide the dialog
    },
    async saveEdit() {
      try {
        // Make the PUT request to update the item
        const response = await axios.put(
          `http://127.0.0.1:8000/items/${this.editedItem.id}`,
          this.editedItem
        );
        console.log("Updated Item:", response.data);

        // Fetch the updated data from the backend after item creation
        const updatedItemsResponse = await axios.get(
          "http://127.0.0.1:8000/items/"
        );

        this.tableData = updatedItemsResponse.data;

        this.dialogVisible = false; // Hide the dialog after saving
      } catch (error) {
        console.error("Error updating item:", error);
      }
    },
    // Show the delete confirmation dialog
    handleDelete(row) {
      this.itemToDelete = { ...row };
      this.deleteConfirmationVisible = true;
    },

    // Close the delete confirmation dialog without deleting the item
    cancelDelete() {
      this.deleteConfirmationVisible = false;
      this.itemToDelete = null;
    },

    // Confirm and delete the item
    async confirmDelete() {
      try {
        const response = await axios.delete(
          `http://127.0.0.1:8000/items/${this.itemToDelete.id}`
        );
        console.log("Deleted Item:", response.data);

        // Remove the item from the local tableData
        const index = this.tableData.findIndex(
          (item) => item.id === this.itemToDelete.id
        );
        if (index !== -1) {
          this.tableData.splice(index, 1);
        }

        // Close the delete confirmation dialog
        this.deleteConfirmationVisible = false;
        this.itemToDelete = null;
      } catch (error) {
        console.error("Error deleting item:", error);
      }
    },
  },
  created() {
    this.fetchItems();
  },
};
</script>
