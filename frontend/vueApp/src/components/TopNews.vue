<template>
  <v-carousel show-arrows="hover" cycle hide-delimiter-background>
    <v-carousel-item
      v-for="i in 3"
      :key="i"
      cover
    >
      <v-card class="mx-auto ma-0 pa-0">
        <v-container fluid style="padding: 0%">
          <v-row no-gutters>
            <v-col :cols="12" md="6" class="ma-0 pa-0">
              <v-card
                :key="data[i * 3]?.id"
                class="ma-0 pa-0"
                style="border-radius: 0"
                @click="handleClick(data[i * 3]?.id)"
              >
                <v-img
                  :src="data[i * 3]?.img"
                  class="align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="500px"
                  cover
                >
                  <v-card-title class="text-white">{{
                    data[i * 3]?.title
                  }}</v-card-title>
                </v-img>
              </v-card>
            </v-col>
            <v-col :cols="12" md="6" class="ma-0 pa-0">
              <v-row no-gutters>
                <v-col
                  :cols="12"
                  class="ma-0 pa-0"
                  v-for="j in 2"
                  :key="j"
                >
                  <v-card
                    :key="data[i * 3 + j + 1]?.id"
                    class="ma-0 pa-0"
                    style="border-radius: 0"
                    @click="handleClick(data[i * 3 + j + 1]?.id)"
                  >
                    <v-img
                      :src="data[i * 3 + j + 1]?.img"
                      class="align-end"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                      height="250px"
                      cover
                    >
                      <v-card-title class="text-white">{{
                        data[i * 3 + j + 1]?.title
                      }}</v-card-title>
                    </v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-carousel-item>
  </v-carousel>
</template>

<!-- かまたデザイン -->
<!-- <template>
  <v-card class="mx-auto ma-0 pa-0">
    <v-container fluid style="padding: 0%">
      <v-row no-gutters>
        <v-col :cols="12" md="6" class="ma-0 pa-0">
          <v-card
            v-for="item in data.slice(0, 1)"
            :key="item.id"
            @click="handleClick(item.id)"
            class="ma-0 pa-0"
            style="border-radius: 0"
          >
            <v-img
              :src="item.img"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="500px"
              cover
              @click="handleClick(item.id)"
            >
              <v-card-title class="text-white">{{ item.title }}</v-card-title>
            </v-img>
          </v-card>
        </v-col>
        <v-col :cols="12" md="6" class="ma-0 pa-0">
          <v-row no-gutters>
            <v-col :cols="12" class="ma-0 pa-0">
              <v-card
                v-for="item in data.slice(1, 2)"
                :key="item.id"
                @click="handleClick(item.id)"
                class="ma-0 pa-0"
                style="border-radius: 0"
              >
                <v-img
                  :src="item.img"
                  class="align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="250px"
                  cover
                  @click="handleClick(item.id)"
                >
                  <v-card-title class="text-white">{{
                    item.title
                  }}</v-card-title>
                </v-img>
              </v-card>
            </v-col>
            <v-col :cols="12" class="ma-0 pa-0">
              <v-card
                v-for="item in data.slice(2, 3)"
                :key="item.id"
                @click="handleClick(item.id)"
                class="ma-0 pa-0"
                style="border-radius: 0"
              >
                <v-img
                  :src="item.img"
                  class="align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="250px"
                  cover
                  @click="handleClick(item.id)"
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
