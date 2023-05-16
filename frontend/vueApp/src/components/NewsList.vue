<template>
  <div>
    <div v-for="item in data" :key="item.id" class="card">
      <h1>{{ item.title }}</h1>
      <p>{{ item.content }}</p>
      <div v-for="(value, key) in item.keywords" :key="key">
        {{ key }}: {{ value }}
      </div>
    </div>
  </div>
</template>

<script>

import { axios } from '/app/plugins/axios'

export default {
    components: {
    },
    data() {
      return {
        data: []
      }
    },
    mounted() {
      this.get_hoge().then((response) => {
        this.data = response.data;
      })
    },
    methods: {
      get_hoge() {
        return axios.get('/news')
      }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
.card {
  background-color: #ddd;
  border-radius: 5px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}
</style>