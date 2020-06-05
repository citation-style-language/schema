<?xml version="1.0"?>
<xsl:stylesheet xmlns:cs="http://purl.org/net/xbiblio/csl" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- converts CSL 1.0 to 1.1 -->
  <xsl:output method="xml" indent="yes"/>
  <xsl:strip-space elements="*"/>
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- update version number -->
  <xsl:template match="@version[.='1.0']">
    <xsl:attribute name="version">1.1</xsl:attribute>
  </xsl:template>

  <!-- strip elements with these deprecated attribute values -->
  <xsl:template match="//cs:link[@rel='independent-parent']"/>
  <xsl:template match="//cs:link[@rel='template']"/>

</xsl:stylesheet>
