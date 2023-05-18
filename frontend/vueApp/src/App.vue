<template>
  <v-app>
    <v-main>
      <ThreeColum />
    </v-main>
  </v-app>
</template>

<script>
import ThreeColum from './components/three-column.vue'

export default {
  name: 'App',
  components: {
    ThreeColum
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
