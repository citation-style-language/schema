// see https://rawgit.com/zaggino/z-schema/master/benchmark/results.html for a list of schema engines

const { parse } = require('edtf')

function isLevel(date, expected, also3) {
  if (typeof date !== 'string') return false

  try {
    const found = parse(date).level
    return (found <= expected ) || (found === 3 && also3)
  }
  catch (err) {
    return false
  }

  return true
}

const formats = {}
for (const level of [0, 1, 2, 3]) {
  (level => {
    formats[`edtf/${level}`] = date => isLevel(date, level, false)
    if (level < 2) formats[`edtf/${level}+3`] = date => isLevel(date, level, true)
  })(level)
}
module.exports = formats
