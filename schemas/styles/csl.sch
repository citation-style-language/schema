<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:cs="http://purl.org/net/xbiblio/csl">
  <sch:ns uri="http://purl.org/net/xbiblio/csl" prefix="cs"/>
  <sch:pattern>
    <sch:rule context="//cs:text[@macro]">
      <sch:assert test="@macro = /cs:style/cs:macro/@name">This macro call has no corresponding macro.</sch:assert>
    </sch:rule>
    <sch:rule context="//cs:key[@macro]">
      <sch:assert test="@macro = /cs:style/cs:macro/@name">This macro call has no corresponding macro.</sch:assert>
    </sch:rule>
    <sch:rule context="/cs:style/cs:macro">
      <sch:assert test="count(/cs:style/cs:macro/@name[. = current()/@name]) = 1">This macro does not have a unique name.</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
