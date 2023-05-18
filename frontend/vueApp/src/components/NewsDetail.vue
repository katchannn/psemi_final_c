<template>
  <div>
    <img :src="imageSrc" alt="画像の説明">
    <h1>{{ data.title }}</h1>
    <div v-for="(value, key) in data.keywords" :key="key">
      <p>{{ key }}: {{ value }}</p>
    </div>
    <p>{{ data.content }}</p>
    <v-btn to="/" color="primary" class="btn" tile>Back to Home</v-btn>

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
          content: '',
        },
        imageSrc: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ZekiVccFBIrXHIe1c1BBk1Ife1M0o_veVo7RXHR8JBNu40r4_Z4TY7SqSbfHnHIuIWtLrbPd40Dq1Ejdeli9di3E58AWn_em9Ww_KHwe0hI1kSVIJN8Du1OVqHaj1SNGeLTVK6A7qeXG6CommSAEoD7MwHdSlrTpdjfFY7XQKm_4a16ri6_3CHb0/s1600/ms.png',
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