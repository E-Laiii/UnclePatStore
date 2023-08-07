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
      <h1>Uncle Pat Admin Page</h1>
      <img
        alt="Uncle Pat logo"
        src="../assets/logo.png"
        style="width: 200px; height: 200px; display: block; margin: auto;"
      />
      <p class="text-center">This is where you can change/alter your store items.</p>
      <!-- Call AdminMethods -->
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
    // Re-route to adminpage
    goToAdminPage() {
      this.$router.push({ path: "/admin-page" });
    },
    //Authentication 
    authenticate() {
      // Perform authentication logic here
      // Let's just assume a hardcoded admin username and password
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
