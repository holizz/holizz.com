<?xml version="1.0" encoding="us-ascii"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!--<xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" indent="yes" encoding="us-ascii"/>-->
<xsl:output method="text" encoding="us-ascii"/>
<xsl:template match="/">
<xsl:value-of select="foo/bar"/> is a nice bar.
My favourite bat is <xsl:value-of select="foo/bat"/>.
I like to eat: <xsl:value-of select="foo/Eat"/>.
I like to drink <xsl:value-of select="foo/drink"/>.
</xsl:template>
</xsl:stylesheet>
