<template>
  <el-container class="resultsDisplay">
    <el-header>
      <!-- 猫猫图 -->
      <el-avatar
        :size="80"
        fit="fit"
        :src="require('../../assets/cat.png')"
      ></el-avatar>
      <el-input
        placeholder="请输入搜索内容"
        v-model="queryInfo.searchInput"
        class="searchInput"
        @keyup.enter.native="Search"
        clearable
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="Search"
        ></el-button>
      </el-input>
    </el-header>
    <el-main>
      <!-- 路由占位符, 有了这个占位符,通过路由匹配到的组件才会在这里展示 -->
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      queryInfo: {
        searchInput: this.$route.query.searchInput,
        searchResult: [],
      },
    }
  },
  mounted() {
    //  创建时就改好页面的标题，参考百度，取搜索内容作为标题
    document.title = this.$route.query.searchInput + '的搜索结果'
    this.Search()
  },
  methods: {
    // 搜索经验
    async Search() {
      const { data: res } = await this.$http.get('search')
      const exp_array = res['data']['hits']['hits']
      console.log(exp_array)
      this.queryInfo.searchResult = exp_array

      this.$router.push({
        path: '/resultgeneral',
        query: this.queryInfo,
      })
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