// see https://rawgit.com/zaggino/z-schema/master/benchmark/results.html for a list of schema engines

const { parse } = require('edtf')

function testLevel(date, expected, also3) {
  if (date.level) {
    return (date.level <= expected ) || (date.level === 3 && also3)
  }
  else if (Array.isArray(date)) {
    return !date.find(d => !testLevel(d, expected, also3))
  }
  return false
}

function isLevel(date, expected, also3) {
  if (typeof date !== 'string') return false

  try {
    return testLevel(parse(date, { level: also3 ? 3 : expected }), expected, also3)
  }
  catch (err) {
    return false
  }
}

const formats = {}
for (const level of [0, 1, 2, 3]) {
  (level => {
    formats[`edtf/${level}`] = date => isLevel(date, level, false)
    if (level < 2) formats[`edtf/${level}+3`] = date => isLevel(date, level, true)
  })(level)
}
module.exports = formats
