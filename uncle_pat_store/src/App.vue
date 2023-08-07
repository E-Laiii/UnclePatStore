<template>
  <div>
    <template v-if="$route.path === '/login'">
      <router-view />
    </template>
    <template v-else>
      <q-layout view="lHh lpR lFf">
        <q-drawer style="position: fixed; z-index: 1000; color: #F4B941; background-color: #0F1530;" v-model="drawer"
          show-if-above :width="73" :breakpoint="500" side="left">
          <q-list padding>
            <q-item :active="getActiveNav() === '/'" clickable v-ripple>
              <q-item-section avatar @click="goToHome">
                <q-icon name="o_home" />
              </q-item-section>
            </q-item>
            <q-item :active="getActiveNav() === '/addCase'" clickable v-ripple>
              <q-item-section avatar @click="goToAdmin">
                <q-icon name="o_add_box" />
              </q-item-section>
            </q-item>
          </q-list>
        </q-drawer>
        <q-page-container>
          <router-view />
        </q-page-container>
      </q-layout>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      dense: true,
    }
  },
  methods: {
    getActiveNav() {
      return this.$route.path
    },
    goToHome() {
      this.$router.push({ path: '/' })
    },
    goToAbout() {
      this.$router.push({ path: '/about' })
    },
    goToAdmin() {
      this.$router.push({ path: '/admin' })
    }
  }
}
</script>

<style scoped>
.user-info {
  display: flex;
  align-items: center;
}

.notification-icon {
  margin-right: 10px;
}

.user-details {
  display: flex;
  align-items: center;
}

.user-name {
  font-size: 24px;
}

.user-icon {
  margin-right: 5px;
}


.case-label {
  color: #CCCCCC;
  font-size: 36px;
  font-weight: bold;
  margin-top: 20px;
}
</style>