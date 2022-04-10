<template>
  <el-container class="search-Container" direction="vertical">
    <el-main>
      <div class="search-Input">
        <div class="login-Image">
          <!-- 登录的图片 -->
          <img src="../assets/cat.png" alt />
        </div>
        <div>
          <!-- 首页的输入框 -->
          <el-input
            placeholder="请输入搜索内容"
            v-model="queryInfo.searchInput"
            class="input-with-select"
            @keyup.enter.native="Search"
          >
            <el-button slot="append" icon="el-icon-search" @click="Search"></el-button>
          </el-input>
        </div>
        <div class="search-Button">
          <el-button round class="my-Button" @click="Search">开始搜索</el-button>
          <el-button round class="my-Button" @click="SearchAll">全部经验</el-button>
        </div>
      </div>
    </el-main>
    <el-footer>
      <myFooter></myFooter>
    </el-footer>
  </el-container>
</template>

<script>
import myFooter from './BottomBar/myFooter.vue'

export default {
  components: {
    myFooter,
  },
  data() {
    return {
      queryInfo: {
        searchInput: '',
      },
    }
  },
  methods: {
    openNewTab(url) {
      window.open(url)
    },
    // 搜索经验
    async Search() {
      // 清除空格
      this.queryInfo.searchInput = this.queryInfo.searchInput.trim()
      // 如果没有填写搜索内容
      if (this.queryInfo.searchInput == '') {
        this.SearchAll()
      } else {
        // 点击了搜索，切换到结果展示的组件，并且把搜索的内容传递过去
        this.$router.push({
          path: '/results',
          query: this.queryInfo,
        })
      }
    },
    // 展示所有的经验
    async SearchAll() {
      console.log('在首页没有填写搜索内容,直接搜索全部结果')
      this.$router.push({
        path: '/results',
      })
    },
  },
}
</script>

<style lang="less" scoped>
.el-footer {
  height: 30px !important;
  display: flex;
  justify-content: center;
}

.search-Container {
  //   background-color: #2b4b6b;
  height: 100%;
}

.my-Button {
  background-color: #f8f9fa;
}

.search-Input {
  width: 582px;
  // height: 20%;
  background-color: #fff;
  border-radius: 3px;
  // 位置采用绝对位置
  position: absolute;
  // 举例顶部和左边都有50%的差距
  left: 50%;
  top: 50%;
  // 然后再向左，向上位移50%
  transform: translate(-50%, -50%);
  min-height: 200px;
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
.login-Image {
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

.IPC {
  color: #999999 !important;
}
</style>
