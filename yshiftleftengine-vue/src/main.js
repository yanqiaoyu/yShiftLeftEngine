import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
// 导入全局样式
import './assets/css/global.css'

// 导入axios发送ajax请求
import axios from 'axios'

// 测试，生产环境，不同的请求的路径
if (process.env.NODE_ENV == 'production') {
  let host = window.location.host //主机
  axios.defaults.baseURL = 'http://' + host + '/api/auth/'
} else {
  axios.defaults.baseURL = 'http://localhost/dashboard'
}

Vue.config.productionTip = false
// 在Vue的原型上挂载axios，让所有实例都能发送http请求
Vue.prototype.$http = axios

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
