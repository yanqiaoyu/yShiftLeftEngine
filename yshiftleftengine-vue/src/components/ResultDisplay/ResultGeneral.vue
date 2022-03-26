<template>
  <div class="divContainsMainAndOthers" v-loading="isLoading">
    <div class="mainContent">
      <!-- 有搜索内容,展示搜索结果 -->
      <div
        v-if="this.$route.query.searchInput != null && this.$route.query.searchInput != ''"
        class="resultStats"
      >
        找到 {{ queryInfo.searchResult.length }} 条关于
        {{ queryInfo.searchInput }} 的经验 (用时
        {{ queryInfo.searchTookTime / 1000 }} 秒)
      </div>
      <!-- 没有搜索内容,展示全部结果 -->
      <div v-else class="resultStats">
        展示所有经验 ( 用时
        {{ queryInfo.searchTookTime / 1000 }} 秒, 共 {{ queryInfo.searchResult.length }} 条 )
      </div>

      <el-card
        class="card-mainContent"
        shadow="never"
        v-for="exp in queryInfo.searchResult"
        :key="exp._id"
      >
        <!-- 经验标题 -->
        <el-link @click="showResultDetail(exp)" :underline="false" class="exp-title">
          <!-- eslint-disable-next-line -->
          <span v-html="showData(exp._source.title)"></span>
        </el-link>

        <!-- 添加时间以及tag -->
        <div class="exp-ts-and-tags">
          {{ $timeTreatment.formatDate(exp._source.createTime) }}
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
        <div class="exp-backgroud">
          <!-- eslint-disable-next-line -->
          <span class="exp-backgroud" v-html="showData(exp._source.background)"></span>
        </div>

        <!-- 阅读全文 -->
        <div>
          <el-link @click="showResultDetail(exp)" :underline="false">阅读全文 〉</el-link>
        </div>
      </el-card>
      <el-empty
        style="margin-top: 150px"
        v-if="queryInfo.searchResult.length==0 && isLoading == false"
        description="Ooops,暂无相关经验,尝试搜索其他关键字,或查看所有经验"
      ></el-empty>
      <el-backtop :visibility-height="10" target=".el-scrollbar__wrap">
        <div
          style="{
        height: 10%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: #1989fa;
      }"
        >UP</div>
      </el-backtop>
    </div>
    <div class="mainOthers"></div>
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
      isLoading: false,
    }
  },

  watch: {
    '$route.query.searchInput': {
      handler(value) {
        if (value != null) {
          this.queryInfo.searchInput = value
          this.Search()
        } else {
          this.SearchAll()
        }
      },
      immediate: true,
    },
  },
  created() {},

  methods: {
    // 查看经验的细节
    showResultDetail(exp) {
      this.$router.push({
        path: '/resultdetail',
        query: exp,
      })
    },
    async SearchAll() {
      console.log('此次使用的是搜索全部')
      this.isLoading = true
      try {
        const { data: res } = await this.$http.get('search')
        const exp_array = res['data']['hits']['hits']
        console.log('搜索到的结果如下:', res['data'])
        // ES搜索的毫秒数
        this.queryInfo.searchTookTime = res['data']['took']
        // ES搜索的实际结果
        this.queryInfo.searchResult = exp_array
      } catch (e) {
        console.log('按关键字搜索出现了问题:', e)
      }

      this.isLoading = false
    },
    async Search() {
      console.log('此次使用的是按关键字搜索')
      this.isLoading = true
      try {
        const { data: res } = await this.$http.get('search', {
          params: {
            searchInput: this.queryInfo.searchInput.trim(),
          },
        })
        console.log(res)
        // 如果查出来非空, 正常处理
        if (res['data'] != null) {
          const exp_array = res['data']['hits']['hits']
          console.log('搜索到的结果如下:', res['data'])
          // ES搜索的毫秒数
          this.queryInfo.searchTookTime = res['data']['took']
          // ES搜索的实际结果
          this.queryInfo.searchResult = exp_array
        }
        // 否则按差不到东西处理
        else {
          this.queryInfo.searchTookTime = 0
          this.queryInfo.searchResult = []
        }
      } catch (e) {
        console.log('按关键字搜索出现了问题:', e)
      }
      this.isLoading = false
    },
    // 高亮功能:如果标题或者背景命中了搜索的关键字,则修改样式
    showData(val) {
      val = val + ''
      var index = this.checkPara(val, this.queryInfo.searchInput)
      // 如果包含关键字
      if (index != -1) {
        // 如果长度小于等于100
        if (val.length <= 100) {
          // 直接高亮并返回
          return val.replace(
            this.queryInfo.searchInput,
            '<font color="#409EFF">' + this.queryInfo.searchInput + '</font>'
          )
        }
        // 如果长度大于100
        else {
          // 以index为原点,向两边扩散,将长度限制在100
          val = this.shortenStr(val, index)
          return val.replace(
            this.queryInfo.searchInput,
            '<font color="#409EFF">' + this.queryInfo.searchInput + '</font>'
          )
        }
      }
      // 如果不包含关键字
      else {
        // 如果长度小于100
        if (val.length <= 100) {
          // 直接返回
          return val
        }
        // 否则截取
        else {
          return this.shortenStr(val, 0)
        }
      }
    },
    // 判断搜索记录是否包含某个关键字
    checkPara(val, para) {
      if (val.indexOf(para) !== -1 && para !== '') {
        return val.indexOf(para)
      } else {
        return -1
      }
    },
    // 字符串截取
    shortenStr(val, index) {
      var start, end
      // 如果index前面不足50个字符,那么前面的部分就不截取了
      if (index < 50) {
        start = 0
      }
      // 否则,需要进行截取
      else {
        start = index - 50
      }

      // 如果start后面长度不足100,那么后面的部分就不截取了
      if (val.length - start < 100) {
        end = val.length - 1
      }
      // 否则,需要进行截取
      else {
        end = start + 100
      }

      return '...' + val.slice(start, end) + '...'
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