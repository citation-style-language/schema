// see https://rawgit.com/zaggino/z-schema/master/benchmark/results.html for a list of schema engines

const { parse } = require('edtf')

const levels = []
const formats = {}
for (const level of [0, 1, 2]) {
  levels.push(level);

  (function(levels) {
    formats[`edtf/level_${levels.map(l => '' + l).join('+')}`] = function (date) {
      if (typeof date !== 'string') return false

      try {
        return levels.includes(parse(date).level)
      }
      catch (err) {
        return false
      }

      return true
    }
  })(levels)
}
module.exports = formats
