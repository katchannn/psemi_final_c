<template>
  <TopNews @news-clicked="navigateToDetail"/>
  <ListNews @news-clicked="navigateToDetail"/>
</template>

<script>
import TopNews from "./TopNews.vue";
import ListNews from "./ListNews.vue";

export default {
  components: {
    TopNews,
    ListNews,
  },
  methods: {
    navigateToDetail(newsId) {
      this.$router.push({ name: 'Detail', params: { id: newsId } });
    }
  }
};
</script>
