<template>
  <div class="divContainsMainAndOthers">
    <div class="mainContent">
      <div class="resultStats">
        找到 {{ queryInfo.searchResult.length }} 条关于
        {{ queryInfo.searchInput }} 的结果 (用时
        {{ queryInfo.searchTookTime / 1000 }} 秒)
      </div>

      <el-card
        class="card-mainContent"
        shadow="never"
        v-for="exp in queryInfo.searchResult"
        :key="exp._id"
      >
        <!-- 经验标题 -->
        <el-link @click="showResultDetail(exp)" :underline="false" class="exp-title">
          {{ exp._source.title }}
          <!-- eslint-disable-next-line -->
          <span v-html="showData(message)"></span>
        </el-link>

        <!-- 添加时间以及tag -->
        <div class="exp-ts-and-tags">
          2022年1月11日20:14:35
          <div class="tags">
            <el-tag
              v-for="tag in exp._source.tags"
              :key="tag"
              type="info"
              size="mini"
              style="margin-left: 10px;"
            >{{ tag }}</el-tag>
          </div>
        </div>

        <!-- 经验背景 -->
        <div class="exp-backgroud">{{ exp._source.background }}</div>

        <!-- 阅读全文 -->
        <div>
          <el-link @click="showResultDetail(exp)" :underline="false">阅读全文 〉</el-link>
        </div>
      </el-card>

      <div v-for="o in 40" :key="o" class="text item">{{ '列表内容 ' + o }}</div>
    </div>
    <div class="mainOthers">其他展示</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      queryInfo: {
        searchInput: this.$route.query.searchInput,
        searchResult: [],
        searchTookTime: 0,
      },
    }
  },

  watch: {
    '$route.query.searchInput': {
      handler(value) {
        this.queryInfo.searchInput = value
        this.Search()
      },
      immediate: true,
    },
  },

  methods: {
    // 查看经验的细节
    showResultDetail(exp) {
      this.$router.push({
        path: '/resultdetail',
        query: exp,
      })
    },

    async Search() {
      const { data: res } = await this.$http.get('search')
      const exp_array = res['data']['hits']['hits']
      // console.log(res['data'])
      // ES搜索的毫秒数
      this.queryInfo.searchTookTime = res['data']['took']
      // ES搜索的实际结果
      this.queryInfo.searchResult = exp_array
    },

        showData(val) {
      val = val + '';
      if (this.checkPara(val,this.listQuery.queryMessage)||this.checkPara(val,this.listQuery.queryMessage2)
        ||this.checkPara(val,this.listQuery.queryMessage3)) {
        //如果搜索结果记录包含关键字中的任何一个，那么修改样式
        return val.replace(this.listQuery.queryMessage'<font color="#409EFF">' + this.listQuery.prodcd + '</font>')
          .replace(this.listQuery.queryMessage2, '<font color="#409EFF">' + this.listQuery.queryMessage3 + '</font>')
         
      } else {
        return val //不做任何修改
      }
    },

  },
}
</script>

<style lang="less" scoped>
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

// 其他内容
.mainOthers {
  height: 100%;
  flex: 1;
  margin-left: 50px;
}

// 卡片
.card-mainContent {
  // 上下有个15px的空隙，左右则没有，与搜索结果展示与用时对齐
  margin: 15px 0;
  width: 630px;
  height: 200px;
}

.el-card /deep/ .el-card__body {
  padding: 0px !important;
}

// 经验标题
.exp-title {
  color: #202020 !important;
  font: 19.2px sans-serif;
}

// 经验时间和tags
.exp-ts-and-tags {
  color: #999999;
  font: 12px sans-serif;
  position: relative;
  padding-right: 60px;
  min-height: 30px;
  margin: 0.5rem 0;
  line-height: 1.5rem;
}

// 经验背景
.exp-backgroud {
  color: #999999;
  font: 18px sans-serif;
  height: 60px;
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

//
.tags {
  display: inline-flex;
}
</style>