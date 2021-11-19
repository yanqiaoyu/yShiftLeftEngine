<template>
  <el-container class="resultsDisplay">
    <el-header>
      <!-- 猫猫图 -->
      <el-avatar
        :size="60"
        fit="fit"
        :src="require('../../assets/cat.png')"
      ></el-avatar>
      <el-input
        placeholder="请输入搜索内容"
        v-model="queryInfo.searchInput"
        class="searchInput"
        @keyup.enter.native="Search"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="Search"
        ></el-button>
      </el-input>
    </el-header>
    <el-main>
      <div class="mainContent">
        <el-card class="box-card" v-for="p in 10" :key="p">
          <div v-for="o in 4" :key="o" class="text item">
            {{ '列表内容 ' + o }}
          </div>
        </el-card>
      </div>
      <div class="mainOthers">其他展示</div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  mounted() {
    //  创建时就改好页面的标题，参考百度，取搜索内容作为标题
    document.title = this.$route.query.searchInput
  },
  data() {
    return {
      queryInfo: {
        searchInput: this.$route.query.searchInput,
      },
    }
  },
  methods: {
    // 搜索经验
    async Search() {},
  },
}
</script>

<style lang="less" scoped>
.resultsDisplay {
  height: 100%;
}

.searchInput {
  margin-left: 20px;
  width: 600px;
  height: 40px;
}

.el-header {
  display: flex;
  //   justify-content: space-between;
  align-items: center;
}

.el-main {
  display: flex;
}

.mainContent {
  height: 100%;
  width: 700px;
}

.mainOthers {
  height: 100%;
  flex: 1;
  margin-left: 50px;
}
</style>