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
      <div class="divContainsMainAndOthers">
        <div class="mainContent">
          <div class="resultStats">找到约 90,800 条结果 （用时 0.54 秒）</div>
          <div v-for="p in 100" :key="p">{{ p }}</div>
          <!-- <el-card
            class="card-mainContent"
            shadow="hover"
            v-for="p in 10"
            :key="p"
          >
            <div v-for="o in 4" :key="o" class="text item">
              {{ '列表内容 ' + o }}
            </div>
          </el-card> -->
        </div>
        <div class="mainOthers">其他展示</div>
      </div>
    </el-main>
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
  mounted() {
    //  创建时就改好页面的标题，参考百度，取搜索内容作为标题
    document.title = this.$route.query.searchInput
  },
  methods: {
    // 搜索经验
    async Search() {},
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

// 搜索结果的数量与花费的时间
.resultStats {
  font-size: 14px;
  display: flex;
  align-items: center;
  width: 630px;
  height: 43px;
  color: #70757a;
}

// 搜索结果以card的结果展示
.el-card {
  border: 0;
}

// 用来包裹主体搜索结果以及其与内容的div，用于解决滚动时，header的阴影条消失的问题
.divContainsMainAndOthers {
  overflow-y: auto;
  width: 100%;
  display: flex;
}

// 主体内容
.mainContent {
  height: 100%;
  width: 700px;
  margin-left: 100px;
}

// 其与内容
.mainOthers {
  height: 100%;
  flex: 1;
  margin-left: 50px;
}

// 卡片
.card-mainContent {
  margin-top: 20px;
  width: 630px;
  height: 200px;
}

.el-card /deep/ .el-card__body {
  padding: 0px !important;
}
</style>