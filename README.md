# Schemas describing the Citation Style Language

<!--
When editing this file, use line breaks to separate sentences or phrases, rather than wrapping the text at a fixed character count.
This helps git produce clean diffs and keeps reflowing to minimum.
More info at https://rhodesmill.org/brandon/2012/one-sentence-per-line/
-->

This is the official repository for schemas describing the Citation Style Language (CSL).
Current schemas include:

* [CSL schema](#csl-schema) - describes CSL style and locale XML files
* [CSL-JSON schema](#csl-json-schema) -
  describes a commonly used JSON data model for storing CSL processor input
  (such as bibliographic metadata).

For more information about CSL, visit <https://citationstyles.org>.
For general quesions and discussions have a look at the [CSL-forum](https://discourse.citationstyles.org/).

## CSL Schema

The CSL schema is written in the compact syntax of [RELAX NG](http://relaxng.org/), 
and currently consists of the following files:

* [`csl.rnc`](schemas/styles/csl.rnc)
* [`csl-categories.rnc`](schemas/styles/csl-categories.rnc)
* [`csl-terms.rnc`](schemas/styles/csl-terms.rnc)
* [`csl-types.rnc`](schemas/styles/csl-types.rnc)
* [`csl-variables.rnc`](schemas/styles/csl-variables.rnc)

CSL style and locale files should be validated against `csl.rnc`,
which incorporates the content of the other files.

The CSL schema contains several [Schematron](http://www.schematron.com/) rules to make sure all macros called in a CSL style are actually defined.
Since the popular [Jing](https://github.com/relaxng/jing-trang) XML validator currently ignores embedded Schematron rules, 
we also provide the `csl.sch` Schematron schema, which contains the Schematron rules extracted from the CSL schema.
Jing users can use `csl.sch` to perform a secondary validation of CSL styles.

## CSL-JSON Schema

The CSL-JSON schema is written in [JSON Schema](http://json-schema.org/), 
and currently consists of the following files:

* [`csl-data.json`](schemas/input/csl-data.json)
* [`csl-citation.json`](schemas/input/csl-citation.json)

To render citations and bibliographies, CSL processors not only require CSL style and locale files, but also bibliographic metadata.
The citeproc-js CSL processor [introduced](http://gsl-nagoya-u.net/http/pub/citeproc-doc.html#data-input) a JSON format to store such metadata, 
and this format has since been adopted by various other software products.
The format, also known as "citeproc-JSON", has been codified in the CSL-JSON Schema. This same schema can be used to validate YAML.

**At this point the CSL-JSON schema is not yet fully normative, and care must be taken to ensure compatibility with other tools built around CSL-JSON.**

Whereas `csl-data.json` describes how the metadata of bibliographic items can be stored, 
`csl-citation.json` incorporates `csl-data.json` and adds an additional layer of information to also describe the context in which bibliographic items are cited.
This includes information such as the order in which items are cited, 
which items are cited together in a single citation, etc.

## Licensing

This repository is released under the [MIT license](LICENSE.txt).
