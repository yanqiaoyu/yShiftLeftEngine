<template>
  <el-container class="resultsDisplay">
    <el-header>
      <!-- 猫猫图 -->
      <el-avatar :size="80" fit="fit" :src="require('../../assets/cat.png')"></el-avatar>
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
  </el-container>
</template>

<script>
export default {
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
      // 如果这个页面中，如果搜索框中没有填写搜索内容，且发起了搜索请求，那么参考谷歌的做法，不作响应
      if (this.queryInfo.searchInput.trim() == '') {
        return
      }
      // 搜索的实际请求不要在这里做，传给下一个组件
      this.$router.replace({
        path: '/resultgeneral',
        query: this.queryInfo,
      })
      // 页面标题要随着每次搜索的不同而改变
      document.title = this.queryInfo.searchInput + '的搜索结果'
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
</style>