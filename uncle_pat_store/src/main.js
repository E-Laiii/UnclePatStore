import * as Vue from "vue";
import * as VueRouter from "vue-router";
import { Quasar } from "quasar";
import quasarUserOptions from "./quasar-user-options";
import App from "./App.vue";
import HomePage from "@/views/HomePage";
import AboutPage from "@/views/AboutPage";
import AdminPage from '@/views/AdminPage';
import { createPinia } from "pinia";
const pinia = createPinia();
const routes = [
  // TODO
  { name: "HomePage", path: "/", component: HomePage, props: true },
  { name: "AboutPage", path: "/about", component: AboutPage, props: true },
  { name: "AdminPage", path: "/admin", component: AdminPage, props: true },
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
});

const app = Vue.createApp(App);
app.use(pinia);
app.use(Quasar, quasarUserOptions);
app.use(router).mount("#app");
