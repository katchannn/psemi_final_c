import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import AxiosPlugin from '../plugins/axios'
import router from '../router/router.js'

createApp(App).use(VueAxios, axios)
                           .use(AxiosPlugin)
                           .use(router)
                           .mount('#app')
