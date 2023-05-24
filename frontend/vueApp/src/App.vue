<template>
  <v-app>
    <v-main>
      <v-app-bar color="primary">
    <v-toolbar-title class="headline text-uppercase">
      <span class="font-weight-light">SECURITY</span>
      <span class="font-weight-bold">NEWS AGGREGATOR</span>
    </v-toolbar-title>
  </v-app-bar>

  <!-- <v-app-bar color="primary">
  <v-toolbar-title>
    <v-avatar>
      <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKx6lnebkMoVxrD6i2a9kHJMAK5StxF6UxajtGC-QKg5H7keNnKCBTpf-Bd8WwGeUEEfMG2Ggx08MrkhJWyUl22L9HcF5u4bQjfUVvL0VUOr0pFg3D_XL31sY-zLG7VDiFGPVTewvqYAqdOJK9m6gUKqO6V3YHg5ylRQkhbSZxgEioqOxwvUsuvejm/s1600/hackers.jpg" alt="Logo">
    </v-avatar>
    <span class="ml-3 title font-weight-light">Security</span>
    <span class="title font-weight-bold">News Aggregator</span>
  </v-toolbar-title>
  </v-app-bar> -->
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
