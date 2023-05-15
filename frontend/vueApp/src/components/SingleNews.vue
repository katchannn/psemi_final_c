<template>
  <div>
    <h1>{{ id }}</h1>
    <h1>{{ title }}</h1>
    <h1>{{ content }}</h1>
  </div>
</template>

<script>

import { axios } from '/app/plugins/axios'

export default {
    components: {
    },
    data() {
      return {
        id : '',
        title : '',
        content : '',
      }
    },
    mounted() {
      //get_hoge()の実行結果を変数messageに渡す
      this.get_news().then((response) =>{
        this.id = response.data.id
        this.title = response.data.title
        this.content = response.data.content
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