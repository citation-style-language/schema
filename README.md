https://github.com/citation-style-language/schema/ is the official repository
for the Citation Style Language (CSL) schema.

The CSL schema consists of the files:

* csl.rnc
* csl-categories.rnc
* csl-terms.rnc
* csl-types.rnc
* csl-variables.rnc

CSL styles and locale files can be validated against csl.rnc, which incorporates
the contents of the other four files.

In addition, the repository contains the files csl-data.json and
csl-citation.json, which describe the metadata model used by citeproc-js for its
input data and for embedded citation data in word processor documents,
respectively. At this point these JSON schemas are not yet normative.

For more information, see CitationStyles.org.