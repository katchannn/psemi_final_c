import { createApp } from 'vue'
import App from './App.vue'

// vuetify
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

// axios
import axios from 'axios'
import VueAxios from 'vue-axios'
import AxiosPlugin from '../plugins/axios'

// router
import router from '../router/router.js'

loadFonts()

createApp(App).use(VueAxios, axios)
                           .use(vuetify)
                           .use(AxiosPlugin)
                           .use(router)
                           .mount('#app')