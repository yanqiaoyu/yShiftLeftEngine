<template>
  <div>
    <el-page-header @back="goBack"></el-page-header>
  </div>
</template>

<script>
export default {
  methods: {
    // 返回上一页
    goBack() {
      this.$router.back(-1)
    },
  },
}
</script>

<style>
</style>