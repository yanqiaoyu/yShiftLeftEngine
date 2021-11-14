<template>
  <div class="search-Container">
    <div class="search-Input">
      <div class="login_image">
        <!-- 登录的图片 -->
        <img src="../assets/cat.png" alt />
      </div>
      <div>
        <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <div class="search-Button">
        <el-button round style="background-color: #f8f9fa">开始搜索</el-button>
        <el-button round style="background-color: #f8f9fa">手气不错</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input3: '',
      select: '',
    }
  },
}
</script>

<style lang="less" scoped>
.search-Container {
  //   background-color: #2b4b6b;
  height: 100%;
}

.search-Input {
  width: 582px;
  height: 20%;
  background-color: #fff;
  border-radius: 3px;
  // 位置采用绝对位置
  position: absolute;
  // 举例顶部和左边都有50%的差距
  left: 50%;
  top: 50%;
  // 然后再向左，向上位移50%
  transform: translate(-50%, -50%);
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

.search-Button {
  margin-top: 30px;
  // 位置采用绝对位置
  position: absolute;
  // 举例顶部和左边都有50%的差距
  left: 50%;
  // 然后再向左，向上位移50%
  transform: translate(-50%);
  vertical-align: middle;
  font-size: 20px;
}

// 登录的图片
.login_image {
  width: 130px;
  height: 130px;
  // 给这个图片添加一个正方形的灰色边框
  border: solid #eee;
  // 把边框变成圆角
  border-radius: 50%;
  //图片和边框之间有间距，5px
  padding: 5px;
  // 添加阴影
  box-shadow: 0 0 10px #ddd;

  // 移动这个图片
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  top: -90%;
  background-color: #fff;

  img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
  }
}
</style>
