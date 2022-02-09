<template>
  <div class="center">
    <el-page-header @back="goBack"></el-page-header>
    <div class="header">
      <!-- 标题 -->
      <h1 class="title">{{ exp._source.title }}</h1>
      <!-- tags -->
      <div class="tags">
        <el-tag
          v-for="tag in exp._source.tags"
          :key="tag"
          type="info"
          size="medium"
          style="margin-left: 10px;"
        >{{ tag }}</el-tag>
      </div>
      <!-- 作者，时间，阅读量 -->
      <div class="authorAndTimeAndClicks">
        <div>作者: yanqiaoyu</div>
        <el-divider direction="vertical"></el-divider>
        <div>2020-02-01 12:00:00</div>
        <el-divider direction="vertical"></el-divider>
        <div>点击量: 12</div>
      </div>
    </div>

    <div class="content">
      <h3>问题背景</h3>
      <div>{{ exp._source.background }}</div>

      <h3>根本原因</h3>
      <div>{{ exp._source.rootCause }}</div>

      <h3>测试建议</h3>
      <div>{{ exp._source.testSuggestion }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      exp: {},
    }
  },

  created() {
    this.exp = this.$route.query
    console.log(this.exp)
  },

  methods: {
    // 返回上一页
    goBack() {
      this.$router.back(-1)
    },
  },
}
</script>

<style>
.center {
  margin: 0 auto;
}

.title {
  text-align: center;
  color: #202020;
  font: 24px sans-serif;
}

.tags {
  text-align: center;
}

.authorAndTimeAndClicks {
  display: flex;
  justify-content: center;
  font: 14px sans-serif;
  color: #999999;
  margin: 20px 0;
}

.el-divider {
  padding-top: 5px;
}

.content {
  width: 740px;
}
</style>