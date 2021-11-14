import Vue from 'vue'
import VueRouter from 'vue-router'

import Search from '../components/Search.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Search,
    meta: {
      // 页面标题title
      title: '测试左移经验引擎'
    }
  }
]

const router = new VueRouter({
  routes
})

export default router
