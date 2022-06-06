const formats = require('./formats')

module.exports = function(ajv) {
  for (const [format, validator] of Object.entries(formats)) {
    ajv.addFormat(format, validator)
  }
  return ajv
}
