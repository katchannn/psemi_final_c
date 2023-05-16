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
    mounted() {
      //get_hoge()の実行結果を変数messageに渡す
      this.get_news().then((response) =>{
        this.data = response.data
      })
    },
    methods: {
      //FastAPIにgetをリクエスト
      get_news() {
        return axios.get('/news/1')
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