This is the official repository for schemas describing the Citation Style
Language (CSL). Current schemas include:

* CSL schema - describes CSL style and locale XML files
* CSL-JSON schema - describes a commonly used JSON data model for storing
CSL processor input (such as bibliographic metadata)  

For more information about CSL, visit
[CitationStyles.org](http://citationstyles.org/).

# CSL Schema

The CSL schema is written in the compact syntax of [RELAX
NG](http://relaxng.org/), and currently consists of the following files:

* csl.rnc
* csl-categories.rnc
* csl-terms.rnc
* csl-types.rnc
* csl-variables.rnc

CSL style and locale files should be validated against "csl.rnc", which
incorporates the content of the other files.

The CSL schema contains several [Schematron](http://www.schematron.com/)
rules to make sure all macros called in a CSL style are actually defined.
Since the popular [Jing](https://code.google.com/p/jing-trang/) XML
validator currently ignores embedded Schematron rules, we also provide the
"csl.sch" Schematron schema, which contains the Schematron rules extracted
from the CSL schema. Jing users can use "csl.sch" to perform a secondary
validation of CSL styles.

# CSL-JSON Schema

The CSL-JSON schema is written in [JSON Schema](http://json-schema.org/),
and currently consists of the following files:

* csl-data.json
* csl-citation.json

To render citations and bibliographies, CSL processors not only require CSL
style and locale files, but also bibliographic metadata. The citeproc-js CSL
processor
[introduced](http://gsl-nagoya-u.net/http/pub/citeproc-doc.html#data-input)
a JSON format to store such metadata, and this format has since been adopted
by various other software products. The format, also known as
"citeproc-JSON", has been codified in the CSL-JSON Schema.

***At this point the CSL-JSON schema is not yet fully normative, and care
must be taken to ensure compatibility with other tools built around
CSL-JSON.***

Whereas "csl-data.json" describes how the metadata of bibliographic items
can be stored, "csl-citation.json" incorporates "csl-data.json" and adds an
additional layer of information to also describe the context in which
bibliographic items are cited. This includes information such as the order
in which items are cited, which items are cited together in a single
citation, etc.

## Mendeley CSL-JSON

Mendeley provided the following documentation on their use of CSL-JSON:

Support for the CSL Embedded Citation Object format is available in
Mendeley Desktop 1.0 and later.

The CSL citation data object consists of:

* a required "schema" element of type "string", set to the URI of the schema
* a required "citationID" element of type "string" or "number", set to ???
* a "citationItems" element of type "array", containing "objects" with the data
  of the individual cites. The individual cite object are structured as:

  * a required "id" element of type "string" or "number", set to an unique cite
    ID
  * a "itemData" element of type "object", described in "csl-data.json/#/items",
    containing the metadata of a single bibliographic item (this object is
    returned in citeproc-js by "sys.retrieveItem()")
  * an "uris" element of type "array", which can contain any number of URIs (of
    type "string") to the bibliographic item
  * a "prefix" element of type "string"
  * a "suffix" element of type "string"
  * a "locator" element of type "string"
  * a "label" element of type "string", set to one of the CSL locator types (see
    http://citationstyles.org/downloads/specification.html#locators)
  * a "suppress-author" element of type "string", "boolean" or "number"
  * a "author-only" element of type "string", "boolean" or "number"
* a "properties" element of type "object" containing:
  * a "noteIndex" element of type "number", set to the index of the footnote or
    endnote
* (Mendeley-specific) a "mendeley" element of type "object" containing:
  * a "previouslyFormattedCitation" element of type "string", set to the
    rendered output of the cite of the previous rendering round (this can be
    used to determine if the user manually altered the output)
  * a "manualFormatting" element of type "string", set to the user-customized
    output of the cite (this output will be used in favor of the generated
    output)

The method to embed metadata for citations and bibliographies typically varies
between word processors. Currently Mendeley uses:

* For Word for Windows: in-text citations and bibliographies are represented by
  a field code of type "wdFieldAddin" or temporarily represented as a bookmark
  if exporting to OpenOffice
* For OpenOffice: in-text citations are of type
  "com.sun.star.text.ReferenceMark", bibliographies are of type
  "com.sun.star.text.TextSection" or temporarily represented as a bookmark if
  exporting to Word

An example of an embedded citation object from Mendeley:

```
{
    "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json",
    "citationID": "12rsus7rlj",
    "citationItems": [
        {
            "id": "ITEM-1",
            "itemData": {
                "id": "ITEM-1",
                "issued": {
                    "date-parts": [
                        [
                            "2007"
                        ]
                    ]
                },
                "title": "My paper",
                "type": "journal-article"
            },
            "locator": "21",
            "label": "page",
            "uris": [
                "http://www.mendeley.com/documents/?uuid=970e7ce0-8a21-482e-b7d6-e77794a2d37d",
                "http://www.zotero.org/uniqueDocumentId"
            ]
        }
    ],
    "mendeley": {
        "previouslyFormattedCitation": "(2007)",
        "manualFormatting": "2007b"
    },
    "properties": {
        "noteIndex": 1
    }
}
```
