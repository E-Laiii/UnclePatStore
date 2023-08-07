import * as Vue from "vue";
import * as VueRouter from "vue-router";
import { Quasar } from "quasar";
import quasarUserOptions from "./quasar-user-options";
import App from "./App.vue";
import HomePage from "@/views/HomePage";
import AdminPage from '@/views/AdminPage';
import { createPinia } from "pinia";

//Create Pinia
const pinia = createPinia();

// Creating routes 
const routes = [
  { name: "HomePage", path: "/", component: HomePage, props: true },
  { name: "AdminPage", path: "/admin", component: AdminPage, props: true },
];

// Creating router
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
});

//Creating the App
const app = Vue.createApp(App);
app.use(pinia);
app.use(Quasar, quasarUserOptions);
app.use(router).mount("#app");
