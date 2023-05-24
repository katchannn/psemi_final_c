<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="primary">
    <v-toolbar-title class="headline text-uppercase">
      <span class="font-weight-light">SECURITY</span>
      <span class="font-weight-bold">NEWS AGGREGATOR</span>
    </v-toolbar-title>
  </v-app-bar> -->

  <v-app-bar color="primary">
  <v-toolbar-title>
    <v-avatar>
      <img src="/isl_icon.png" width="40" height="45">
    </v-avatar>
    <span class="ml-3 title font-weight-light">Security</span>
    <span class="title font-weight-bold">News Aggregator</span>
  </v-toolbar-title>
  </v-app-bar>
     <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
