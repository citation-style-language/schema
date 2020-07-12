# How to Contribute

## Pull Requests

We encourage pull requests. Please use the following guidelines:

- in general, follow [these recommendations](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) on writing good commit messages
- make sure your PRs are focused, and link where possible to existing issues
- follow  the instructions on the PR template

## Issues

Regardless of the change, however, the current status of CSL requires us to be fairly conservative. For issue reports, please follow the template instructions, and include all specified information. It's important for us to be able to quickly understand what you are requesting, how broad the need is, and what implementation options there are.

## Versioning

### Changes to the CSL Schema

At this point, changes to the CSL RELAX NG schema consist of the following:

<dl>
  <dt>Changes to csl-categories.rnc, csl-terms.rnc, csl-types.rnc, or csl-variables.rnc</dt>
  <dd>Adding new variables, item types, locators, or terms; these can usually be added to minor x.x.x version changes.</dd>
  <dt>Changes to csl.rnc</dt>
  <dd>These are often more significant and may have an impact on compatability, and so are typically reserved for major x.x version changes.</dd>
</dl>

### Changes to the CSL-JSON Schema

The data schemas are intended to mirror the `rnc` files, and so follow similar conventions. Ideally when we add variables, we add to both at the same time.

## Pre-Commit Hooks

The repository includes a [pre-commit](https://pre-commit.com) configuration file, and a pre-commit hook, which will run linters for changes on any `rnc`, `json`, or `yaml` files. 
To install them, do the following from your local repo:

``` console
pip install pre-commit
pre-commit install
```

