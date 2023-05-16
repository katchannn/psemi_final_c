<template>
  <div>
    <h1>{{ data.title }}</h1>
    <div v-for="(value, key) in data.keywords" :key="key">
      <h1>{{ key }}: {{ value }}</h1>
    </div>
    <h1>{{ data.content }}</h1>
  </div>
</template>

<script>

import { axios } from '/app/plugins/axios'

export default {
    components: {
    },
    data() {
      return {
        data: {
          id: null,
          title: '',
          keywords: {},
          content: ''
        }
      }
    },
    created() {
      const id = this.$route.params.id;
      this.get_details(id).then((response) =>{
        this.data = response.data
      })
    },
    methods: {
      get_details(id) {
      return axios.get(`/news/${id}`) // idに基づいたデータを取得します
      }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>