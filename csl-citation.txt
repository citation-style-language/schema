CSL Embedded Citation Object Format
-----------------------------------

The JSON schema "csl-citation.json" describes a format for embedding citation
objects in documents. The JSON schema references "csl-data.json", which
describes the CSL citation data object format for CSL processors (documented at
http://gsl-nagoya-u.net/http/pub/citeproc-doc.html#citation-data-object).

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

If you are trying to implement this and want help ensuring compatibility or have
suggestions for changes, please use the xbiblio mailing list:
https://lists.sourceforge.net/lists/listinfo/xbiblio-devel

An example of an embedded citation object from Mendeley (the "Mendeley
Citation{970e7ce0-8a21-482e-b7d6-e77794a2d37d}" part is not required and used
only for backwards compatibility with older versions of Mendeley, any text before
"CSL_CITATION" can be ignored, and newlines have been added for readability):

---
ADDIN Mendeley Citation{970e7ce0-8a21-482e-b7d6-e77794a2d37d} CSL_CITATION
{
	"schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json",
	"citationID":"12rsus7rlj",
	"citationItems":
	[
		{
			"id":"ITEM-1",
			"itemData":
			{
				"id" : "ITEM-1",
				"issued" : { "date-parts" : [ [ "2007" ] ] },
				"title" : "My paper",
				"type" : "journal-article"
			},
			"locator":"21",
			"label":"page",
			"uris" : 
			[ 
				"http://www.mendeley.com/documents/?uuid=970e7ce0-8a21-482e-b7d6-e77794a2d37d",
				"http://www.zotero.org/uniqueDocumentId"
			]
		}
	],
	"mendeley":
	{
		"previouslyFormattedCitation" : "(2007)",
		"manualFormatting" : "2007b"
	}
	"properties":
	{
		"noteIndex": 1
	}
}
---

An example of a bibliography field code contents from Mendeley (the "Mendeley
Bibliography" part is not required and only used by Mendeley for backwards compatibility)

---
ADDIN Mendeley Bibliography CSL_BIBLIOGRAPHY
---
