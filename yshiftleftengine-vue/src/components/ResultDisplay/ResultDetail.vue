<template>
  <div class="center">
    <div class="header">
      <!-- 经验标题 -->
      <h1 class="title">{{ exp._source.title }}</h1>
      <!-- 经验的tags -->
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
      <div class="others">123</div>
    </div>
    <div>{{ exp._source.background }}</div>
    <div>{{ exp._source.rootCause }}</div>
    <div>{{ exp._source.testSuggestion }}</div>
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
</style>