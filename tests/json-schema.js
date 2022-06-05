const schema = {
  type: "object",
  properties: {
    baz: { type: 'string', format: 'edtf/level_0+1' }
  },
  required: ['baz'],
  additionalProperties: false
}

const formats = require('../validator/formats')

const Ajv = require("ajv")
const ajv = require('../validator/ajv')(new Ajv)

const ZSchema = require('../validator/z-schema')(require('z-schema'))
const zschema = new ZSchema

const IMJV = require('is-my-json-valid')
const imjv = IMJV(schema, { formats })

const JSEN = require('jsen')
const jsen = JSEN(schema, { formats })

for (const data of [{baz: '2016-XX'}, {baz: 'invalid'}]) {
  if (!ajv.validate(schema, data)) console.log('ajv', data, ajv.errors[0].message)
  if (!zschema.validate(data, schema)) console.log('zschema', data, zschema.getLastError().details[0].message)
  if (!imjv(data)) console.log('imjv', data, imjv.errors[0].message)
  if (!jsen(data)) console.log('jsen', data, jsen.errors[0])
}
