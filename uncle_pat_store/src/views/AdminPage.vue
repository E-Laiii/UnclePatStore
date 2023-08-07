<template>

  <div>
    <!-- Admin Authentication Modal -->
    <q-dialog v-model="showModal">
      <q-card>
        <q-card-section>
          <q-input v-model="username" label="Username" />
          <q-input v-model="password" label="Password" type="password" />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn @click="authenticate" label="Login" color="primary" />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <!-- Admin Page Content -->
    <div v-if="loggedIn">
      <h1>Admin Page</h1>
      <p>This is where you can change/alter your store items.</p>
      <!-- Rest of the admin page content goes here -->
      <add-item @add-item="handleAddItem" />
    </div>
  </div>
  <div></div>
</template>

<script>
// import axios from 'axios';
import AddItem from "../components/AdminMethods.vue";

export default {
  name: "App",
  components: {
    AddItem,
  },
  data() {
    return {
      showModal: true,
      username: "",
      password: "",
      loggedIn: false,
      items: [],
    };
  },
  methods: {
    goToAdminPage() {
      this.$router.push({ path: "/admin-page" });
    },
    authenticate() {
      // Perform authentication logic here (e.g., check credentials against server)
      // For simplicity, let's just assume a hardcoded admin username and password
      const adminUsername = "adminpat";
      const adminPassword = "adminpat";

      if (this.username === adminUsername && this.password === adminPassword) {
        // Successful authentication
        this.loggedIn = true;
        this.showModal = false;
      } else {
        // Invalid credentials, show an error message or handle as needed
        alert("Invalid credentials. Please try again.");
      }
    },

  },
};
</script>
