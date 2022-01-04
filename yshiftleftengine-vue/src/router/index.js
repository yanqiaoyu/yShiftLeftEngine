import Vue from 'vue'
import VueRouter from 'vue-router'

import Search from '../components/Search.vue'
import Results from '../components/ResultDisplay/Results.vue'
import ResultsDetail from '../components/ResultDisplay/ResultDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Search,
    meta: {
      // 页面标题title
      title: '测试左移经验引擎'
    }
  },
  {
    path: '/results',
    component: Results,
    meta: {
      // 页面标题title
      title: ''
    }
  },
  {
    path: '/resultdetail',
    component: ResultsDetail,
    meta: {
      // 页面标题title
      title: ''
    }
  }
]

const router = new VueRouter({
  routes
})

export default router
