import { createRouter, createWebHistory } from 'vue-router';
import NewsDetail from '../src/components/NewsDetail.vue'
import NewsList from '../src/components/NewsList.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'NewsList',
            component: NewsList
          },
          {
            path: '/details/:id', // idパラメータを持つdetailsルートを設定します
            name: 'NewsDetail',
            component: NewsDetail
          }
    ],
  });

export default router;
