<template>
    <div>
      <v-card>
        <div
          v-for="item in data"
          :key="item.id"
          class="card"
          @click="handleClick(item.id)"
        >
          <img :src="imageSrc" alt="画像の説明" />
          <h1>{{ item.title }}</h1>
          <div v-for="(value, key) in item.keywords" :key="key">
            {{ key }}: {{ value }}
          </div>
        </div>
      </v-card>
    </div>
  </template>
  
  <script>
  import { axios } from "/app/plugins/axios";
  
  export default {
    components: {},
    data() {
      return {
        imageSrc:
          "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ZekiVccFBIrXHIe1c1BBk1Ife1M0o_veVo7RXHR8JBNu40r4_Z4TY7SqSbfHnHIuIWtLrbPd40Dq1Ejdeli9di3E58AWn_em9Ww_KHwe0hI1kSVIJN8Du1OVqHaj1SNGeLTVK6A7qeXG6CommSAEoD7MwHdSlrTpdjfFY7XQKm_4a16ri6_3CHb0/s1600/ms.png",
        data: [],
      };
    },
    mounted() {
      this.get_hoge().then((response) => {
        this.data = response.data;
      });
    },
    methods: {
      get_hoge() {
        return axios.get("/news");
      },
      handleClick(id) {
        this.$emit('news-clicked', id);
      },
    },
  };
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
    cursor: pointer;
  }
  </style>
  