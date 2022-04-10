<template>
  <!-- 这个组件用来存放底部 -->
  <div>
    <el-link
      :underline="false"
      target="_blank"
      href="https://beian.miit.gov.cn"
      class="IPC"
    >粤ICP备2022026889号</el-link>
    <el-divider direction="vertical"></el-divider>
    <img src="../../assets/备案图标.png" alt />
    <el-link
      :underline="false"
      target="_blank"
      href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=44030602006714"
      class="IPC"
    >粤公网安备 44030602006714号</el-link>
  </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>
.IPC {
  color: #999999 !important;
}
</style>
