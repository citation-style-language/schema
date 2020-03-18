# Introduction

These are XSD representations of the RNC schema files, for developers that 
may need them.

# Warning on XSD Limitations

RNG has some features (like interleave) that we make use of in 
CSL that are not supported in XSD. This should mean the XSD representations 
is slightly less strict than the RNC version.

The specifc warning from Trang is:

```
csl.rnc:619:8: warning: choice between attributes and children cannot be represented; approximating
```

That line in the RNC file corresponds to the specification of the cs:date element.
