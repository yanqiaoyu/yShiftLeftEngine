export default {
     addZero(num) {
        return num < 10 ? '0' + num : num
      },
        // 格式化带时区的时间
         formatDate(date) {
            var arr = date.split('T')
            var d = arr[0]
            var darr = d.split('-')
            var t = arr[1]
            var tarr = t.split('.000')
            var marr = tarr[0].split(':')
            var dd =
              parseInt(darr[0]) +
              '/' +
              parseInt(darr[1]) +
              '/' +
              parseInt(darr[2]) +
              ' ' +
              parseInt(marr[0]) +
              ':' +
              parseInt(marr[1]) +
              ':' +
              parseInt(marr[2])
            return this.formatDateTime(dd)
          },
      
           formatDateTime(date) {
            let time = new Date(Date.parse(date))
            time.setTime(time.setHours(time.getHours() + 8))
            let Y = time.getFullYear() + '-'
            let M = this.addZero(time.getMonth() + 1) + '-'
            let D = this.addZero(time.getDate()) + ' '
            let h = this.addZero(time.getHours()) + ':'
            let m = this.addZero(time.getMinutes()) + ':'
            let s = this.addZero(time.getSeconds())
            return Y + M + D + h + m + s
          }
}

