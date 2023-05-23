<template>
  <DetailNews :news-id="id"/>
</template>

<script>
import DetailNews from "./DetailNews.vue";

export default {
  components: {
    DetailNews,
  },
  props: {
    id: String
  }
};
</script>
