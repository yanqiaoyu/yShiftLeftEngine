<template>
  <el-container class="resultsDisplay">
    <el-header>
      <!-- 猫猫图 -->
      <el-avatar
        :size="80"
        fit="fit"
        :src="require('../../assets/cat.png')"
        @click.native="return2Index"
      ></el-avatar>
      <!-- 搜索界面的输入框 -->
      <el-input
        placeholder="请输入搜索内容"
        v-model="queryInfo.searchInput"
        class="searchInput"
        @keyup.enter.native="Search"
        clearable
      >
        <el-button slot="append" icon="el-icon-search" @click="Search"></el-button>
      </el-input>
    </el-header>
    <el-scrollbar style="height:100%">
      <el-main>
        <!-- 路由占位符, 有了这个占位符,通过路由匹配到的组件才会在这里展示 -->
        <!-- 这里对应着2个组件，一个是所有搜索结果的展示，一个是单个搜索结果细节的展示 -->
        <router-view></router-view>
      </el-main>
    </el-scrollbar>
    <el-footer>
      <my-footer></my-footer>
    </el-footer>
  </el-container>
</template>

<script>
import myFooter from '../BottomBar/myFooter.vue'

export default {
  components: {
    myFooter,
  },
  data() {
    return {
      queryInfo: {
        searchInput: this.$route.query.searchInput,
      },
    }
  },
  created() {
    this.Search()
  },
  methods: {
    // 搜索经验
    async Search() {
      // 搜索的实际请求不要在这里做，传给下一个组件
      if (
        this.queryInfo.searchInput != null &&
        this.queryInfo.searchInput != ''
      ) {
        // 清除空格
        this.queryInfo.searchInput = this.queryInfo.searchInput.trim()

        this.$router.replace({
          path: '/resultgeneral',
          query: this.queryInfo,
        })
        // 页面标题要随着每次搜索的不同而改变
        document.title = this.queryInfo.searchInput + '的搜索结果'
      } else {
        this.$router.replace({
          path: '/resultgeneral',
        })
        document.title = '所有搜索结果'
      }
    },
    // 回首页
    return2Index() {
      this.$router.replace('/')
    },
    openNewTab(url) {
      window.open(url)
    },
  },
}
</script>

<style lang="less" scoped>
// 整个大的el-container
.resultsDisplay {
  height: 100%;
}

// 搜索输入框
.searchInput {
  margin-left: 20px;
  width: 650px;
  height: 40px;
}

// 顶部
.el-header {
  display: flex;
  align-items: center;
  height: 100px !important;
  // 添加阴影
  box-shadow: 0 0 10px #ddd !important;
}

// 主体
.el-main {
  display: flex;
  overflow: hidden;
  padding: 1px !important;
}

.el-footer {
  height: 30px !important;
  display: flex;
  justify-content: center;
}
</style>