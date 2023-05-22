import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../src/components/HomeView.vue'
import DetailView from '../src/components/DetailView.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: HomeView
          },
          {
            path: '/details/:id', 
            name: 'Detail',
            component: DetailView,
            props: true
          }
    ],
  });

export default router;
