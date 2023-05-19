<template>
  <v-app>
    <v-main>
     <!-- <router-view /> -->
      <HomeView />
      <DetailView />
    </v-main>
  </v-app>
</template>

<script>
import HomeView from './components/HomeView.vue'
import DetailView from './components/DetailView.vue';

export default {
  name: 'App',
  components: {
    HomeView,
    DetailView
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
