<template>
  <NewsDetail />
</template>

<script>
import NewsDetail from './components/NewsDetail.vue'

export default {
  name: 'App',
  components: {
    NewsDetail
  }
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
