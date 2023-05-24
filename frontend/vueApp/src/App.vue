<template>
  <v-app>
    <v-main>
      <header-view />
      <router-view />
      <footer-view />
    </v-main>
  </v-app>
</template>

<script>
import HeaderView from '../src/components/HeaderView.vue';
import FooterView from '../src/components/FooterView.vue';

export default {
  name: "App",
  components: {
    HeaderView,
    FooterView
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
