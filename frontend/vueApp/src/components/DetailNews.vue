<template>
  <div style="max-width: 800px; margin: auto; padding: 20px; box-shadow: 0px 5px 15px rgba(0,0,0,0.1); border-radius: 10px; position: relative;">
    
    <v-btn to="/" color="red" class="btn" tile style="position: absolute; top: 20px; left: 20px;"> <v-icon>mdi-close-thick</v-icon></v-btn>
    
    <img :src="data.img" alt="画像の説明" style="width: 100%; height: auto; border-radius: 10px 10px 0 0;" />
    
    <div style="padding: 20px;">
      <h1 style="color: #333; font-size: 2em; margin-bottom: 5%;">{{ data.title }}</h1>
      
      <div v-for="(value, key) in data.keywords" :key="key" style="margin-bottom: 10px; text-align: left; margin: 2% 0;">
        <div style="font-size: 1.2em; color: #666;"><strong>{{ key }}</strong></div>
        <div style="font-size: 1.2em; color: #333; line-height: 1.5;">{{ value }}</div>
      </div>
      
      <p style="font-size: 1.2em; color: #333; line-height: 1.5; margin-top: 5%; text-align: left;">{{ data.content }}</p>
    </div>

    <v-btn
        class="ma-2"
        color="primary"
        icon="mdi-transfer-up"
        @click="scrollToTop"
      ></v-btn>
  </div>
</template>






<script>
import { axios } from "/app/plugins/axios";

export default {
  props: {
    newsId: String,
  },
  data() {
    return {
      data: {
        id: null,
        img: "",
        html : "",
        title: "",
        keywords: {},
        content: "",
      },
    };
  },
  created() {
    const id = this.newsId;
    this.get_details(id).then((response) => {
      this.data = response.data;
    });
  },
  methods: {
    get_details(id) {
      return axios.get(`/news/${id}`); // idに基づいたデータを取得します
    },
    scrollToTop() {
      window.scrollTo(0, 0);
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
