import Vue from 'vue'
import VueRouter from 'vue-router'

import Search from '../components/Search.vue'
import Results from '../components/ResultDisplay/Results.vue'
import ResultDetail from '../components/ResultDisplay/ResultDetail.vue'
import ResultGeneral from '../components/ResultDisplay/ResultGeneral.vue'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err)
}

const originalReplace = VueRouter.prototype.replace
VueRouter.prototype.replace = function push(location) {
  return originalReplace.call(this, location).catch((err) => err)
}

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
    },
    children: [
      { path: '/resultdetail', component: ResultDetail, meta: { title: '' } },
      { path: '/resultgeneral', component: ResultGeneral, meta: { title: '' } }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
