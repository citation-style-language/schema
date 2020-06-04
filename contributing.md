# How to Contribute

## Schema Changes

At this point, changes to CSL RelaxNG schema consist of the following:

<dl>
  <dt>Changes to csl-terms.rnc, csl-types.rnc, or csl-variables.rnc.</dt>
  <dd>Adding new variables, itemtypes, locators, or terms; these can usually be added to minor x.x.x version changes.</dd>
  <dt>Changes to csl.rnc.</dt>
  <dd>These are typically structural changes that may have an impact on compatability, and are typically reserved for major x.x version changes.</dd>
</dl>

Regardless of the change, however, the current status of CSL requires us to be fairly conservative about change. So for either issue reports, please use the correct template, and include all specified information. It's important for us to be able to quickly understand what you asking for, how broad the need is, and what implementations options there are.

## Pull Requests

We encourage pull requests. Please follow the following guidelines:

- in general, please follow [these recommendations](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) on writing good commit messages
- reference existing issues, or create and reference new ones, that clearly lay out the issue your PR is addressing
- if you are merely adding a string to `csl-terms.rnc`, `csl-types.rnc`, or `csl-variables`:
   - please start your commit message with "Add" and specify which type of string you are adding; for example `Add "foo" and "bar" type`
   - if you find your first line commit message is over 50 characters, that may suggest you PR should be split up
   - make sure to add the string(s) to the `csl-data.json` schema as well in your commit
- if you are proposing any change to `csl.rnc`, be careful. This is the file that describes the basic model of CSL, and so changes here have the potential to break implementations. If you feel you must request a breaking change, please include the word "breaking" in the body of your commit message, as our changelog tool will pick that up.
- if you are suggesting deprecating anything, please including the word "deprecate" in the body of your commit message
