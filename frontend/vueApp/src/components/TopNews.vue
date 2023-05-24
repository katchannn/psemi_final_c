<!-- <template>
  <v-card class="mx-auto" max-width="500">
    <v-container fluid>
      <v-row dense>
        <v-col :cols="12" md="6" class="h-100">
          <v-card
            v-for="item in data.slice(0, 1)"
            :key="item.id"
            class="card"
            @click="handleClick(item.id)"
          >
            <v-img
              :src="item.imageSrc"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="400px"
              cover
            >
              <v-card-title class="text-white">{{ item.title }}</v-card-title>
            </v-img>
          </v-card>
        </v-col>
        <v-col :cols="6" md="6">
          <v-row dense>
            <v-col :cols="12">
              <v-card
                v-for="item in data.slice(1, 2)"
                :key="item.id"
                class="card"
                @click="handleClick(item.id)"
              >
                <v-img
                  :src="item.imageSrc"
                  class="align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="200px"
                  cover
                >
                  <v-card-title class="text-white">{{
                    item.title
                  }}</v-card-title>
                </v-img>
              </v-card>
            </v-col>
            <v-col :cols="12">
              <v-card
                v-for="item in data.slice(2, 3)"
                :key="item.id"
                class="card"
                @click="handleClick(item.id)"
              >
                <v-img
                  :src="item.imageSrc"
                  class="align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="200px"
                  cover
                >
                  <v-card-title class="text-white">{{
                    item.title
                  }}</v-card-title>
                </v-img>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template> -->

<template>
  <v-carousel show-arrows="hover" cycle hide-delimiter-background>
    <v-carousel-item
      v-for="item in data.slice(0, 3)"
      :key="item.id"
      @click="handleClick(item.id)"
      cover
    >
      <v-img
        :src="item.img"
        class="align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="100%"
        cover
      >
        <v-card
          class="d-flex flex-column"
          color="transparent"
          flat
          height="100%"
        >
          <v-spacer />
          <v-card-title class="mb-12 text-white">
            {{ item.title }}
          </v-card-title>
        </v-card>
      </v-img>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { axios } from "/app/plugins/axios";

export default {
  components: {},
  data() {
    return {
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
      this.$emit("news-clicked", id);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>
