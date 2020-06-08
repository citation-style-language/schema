# How to Contribute

## Schema Changes

At this point, changes to the CSL RelaxNG schema consist of the following:

<dl>
  <dt>Changes to csl-terms.rnc, csl-types.rnc, or csl-variables.rnc.</dt>
  <dd>Adding new variables, itemtypes, locators, or terms; these can usually be added to minor x.x.x version changes.</dd>
  <dt>Changes to csl.rnc.</dt>
  <dd>These are often more significant and may have an impact on compatability, and so are typically reserved for major x.x version changes.</dd>
</dl>

Regardless of the change, however, the current status of CSL requires us to be fairly conservative. For issue reports, please the template instructions, and include all specified information. It's important for us to be able to quickly understand what you are requesting, how broad the need is, and what implementation options there are.

## Pull Requests

We encourage pull requests. Please follow the following guidelines:

- make sure your PRs and reasonably focused, and link where possible to existing issues
- for linting and formatting the schema files, please use [trang](https://github.com/relaxng/jing-trang) for the rnc (see the [trang script](https://github.com/citation-style-language/schema/blob/master/tools/rnc-validate-format.sh)), and use [prettier](https://prettier.io) for the json
- in general, please follow [these recommendations](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) on writing good commit messages
- follow  the instructions on the template
