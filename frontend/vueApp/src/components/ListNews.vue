<template>
  <v-container style="padding: 0 10%">
    <div style="text-align: left; margin: 3% 0 3% 3%">
      <h1>News</h1>
    </div>
    <v-row>
      <v-col
        v-for="item in data"
        :key="item.id"
        cols="12"
        sm="12"
        md="6"
        lg="6"
        class="mb-4"
      >
        <v-card
          class="mx-auto d-flex flex-column"
          max-width="90%"
          height="100%"
          @click="handleClick(item.id)"
        >
          <v-img
            class="align-end text-white"
            height="300"
            :src="imageSrc"
            cover
          ></v-img>

          <v-card-text style="text-align: left">
            <h3>{{ item.title }}</h3>
          </v-card-text>

          <v-card-actions class="mt-auto">
            <v-chip
              v-for="(value, key) in item.keywords"
              :key="key"
              color="orange"
            
              
            >
              {{ key }}
            </v-chip>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
      this.$emit("news-clicked", id);
    },
  },
};
</script>
