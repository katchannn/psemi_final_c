<template>
  <v-app-bar color="primary" @click="goHome" style="cursor: pointer">
    <v-toolbar-title>
      <span class="ml-3 title font-weight-light">Security</span>
      <span class="title font-weight-bold">News Aggregator</span>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>
