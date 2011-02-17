<?xml version="1.0" encoding="us-ascii"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" indent="yes" encoding="us-ascii"/>
<xsl:template match="/">
<html>
<head>
<title>Yo</title>
</head>
<body>
<p><xsl:value-of select="foo/bar"/> is a nice bar.</p>
<p>My favourite bat is <xsl:value-of select="foo/bat"/>.</p>
<p>I like to eat: <xsl:value-of select="foo/Eat"/>.</p>
<p>I like to drink <xsl:value-of select="foo/drink"/>.</p>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
