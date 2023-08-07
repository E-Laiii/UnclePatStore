<template>
  <div>
    <h2>Updating Items:</h2>
    <!-- Form for adding items -->
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

    <!-- Your table to display existing items -->
    <q-page style="margin-top: 20px;">
      <q-table :rows="tableData" :columns="tableColumns">
        <!-- 'actions' column -->
        <template v-slot:body-cell-actions="{ row }">
          <q-td>
            <q-btn @click="handleEdit(row)" label="Edit" color="primary" />
            <q-btn @click="handleDelete(row)" label="Delete" color="negative" />
          </q-td>
        </template>
      </q-table>

      <!-- Dialog for updating the item row -->
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

      <!-- Dialog for deleting the item row -->
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
        // id section
        {
          name: "id",
          required: true,
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        // name section
        {
          name: "name",
          align: "left",
          label: "Name",
          field: "name",
          sortable: true,
        },
        // description section
        {
          name: "description",
          align: "left",
          label: "Description",
          field: "description",
          sortable: true,
        },
        // price section
        {
          name: "price",
          align: "left",
          label: "Price",
          field: "price",
          sortable: true,
        },
        // action section
        {
          name: "actions",
          align: "left",
          label: "Actions",
          field: "id", 
          format: () => {
            return `
              <q-btn @click="handleEdit(row)" label="Edit" color="primary" />
              <q-btn @click="handleDelete(row)" label="Delete" color="negative" />
            `;
          },
        },
      ],
    };
  },
  methods: {
    // Get items from fastapi and show in table
    async fetchItems() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/items/");
        this.tableData = response.data;
      } catch (error) {
        console.error("Error fetching items:", error);
      }
    },
    // Adding items into store
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

        // Update the table
        this.tableData = updatedItemsResponse.data;

      } catch (error) {
        console.error("Error adding item:", error);
      }

      // Clear the input fields after adding the item
      this.itemName = "";
      this.itemDescription = "";
      this.itemPrice = 0;
    },
    // Show dialog if edit button is chosen
    async handleEdit(row) {
      // Set the editedItem with the values of the selected row
      this.editedItem = { ...row };
      this.dialogVisible = true; // Show the dialog
    },
    // Close the edit dialog without editing the item
    cancelEdit() {
      this.dialogVisible = false; // Hide the dialog
    },
    // Updating the item
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

        // Show updated table
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
