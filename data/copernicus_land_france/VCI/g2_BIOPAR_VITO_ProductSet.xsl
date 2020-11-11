<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:gco="http://www.isotc211.org/2005/gco" xmlns:gml="http://www.opengis.net/gml">
	<!--author: Bruno Smets, VITO: bruno.smets@vito.be> -->
	<!--version: 2.5, date: 11 juni 2014 -->
        <!--todo: factor-out some common routines -->
	<xsl:template match="/">
		<html>
			<head>
				<title>VITO BioPar DataSet information</title>
			</head>
			<body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
				<a name="top"/>
				<center>
				<h1 style="color:indigo">
					<a name="Top"/>
					<a href="http://land.copernicus.eu/global">
				    <img src="http://copernicus.eu/sites/all/themes/copernicus/logo.png" width="154" height="55"/>
					</a>
					<big>
						<span> Copernicus Global Land Product  </span>
					</big>

				</h1>
				<hr/>
				<pre>
					<a href="#ProductInfo" style="background-color:yellow">ProductInfo |</a>
					<a href="#SpatialInfo" style="background-color:lightblue"> SpatialInfo |</a>
					<a href="#TemporalInfo" style="background-color:yellow"> TemporalInfo |</a>
					<a href="#DistributionInfo" style="background-color:lightblue"> DistributionInfo</a>
				</pre>
				<br />
				<pre>
					<a href="#ProductContent" style="background-color:lightblue"> ProductContent |</a>
					<a href="#ProductQuality" style="background-color:yellow"> ProductQuality |</a>
					<a href="#DataPolicies" style="background-color:lightblue"> DataPolicies |</a>
					<a href="#Contacts" style="background-color:yellow"> Contacts |</a>
					<a href="#ExtraInfo" style="background-color:lightblue"> ExtraInfo |</a>
				</pre>
				</center>
				<hr/>
				<xsl:apply-templates select="gmd:MD_Metadata"/>
				<hr/>
					Application developed by 
					<a href="http://www.vito.be">
						<img src="http://endeleo.vgt.vito.be/images/vito_1.jpg" />
					</a>
        (c) 2013, apr16, version 2.3
			</body>
		</html>
	</xsl:template>
  
	<!-- Main table creation -->
	<xsl:template match="gmd:MD_Metadata">
		<p>
      <!-- Create first all product information stuff using identificationInfo -->
			<xsl:apply-templates select="gmd:identificationInfo"/>
      <!-- Next create actual content product information stuff -->
      <!-- Header defined here to avoid multiple when loop over contentInfo -->
      <xsl:if test="gmd:contentInfo/gmd:MD_CoverageDescription">
        <h2 style="margin-bottom: 0;">
          <a name="ProductContent"/>
          <strong>Product Content</strong>
        </h2>
        <xsl:apply-templates select="gmd:contentInfo"/>
        <a href="#Top">back to top</a>
      </xsl:if>
      <!-- Last end with data policies & contacts, use artificially distributionInfo -->
      <xsl:apply-templates select="gmd:distributionInfo"/>
		</p>
	</xsl:template>
  
	<!-- Identification tables creation -->
	<xsl:template match="gmd:identificationInfo">
		<!-- generic description information -->
		<xsl:call-template name="DescriptionTemplate">
             </xsl:call-template>
		<!-- spatial information - assume always bounding rectangle -->
		<xsl:call-template name="SpatialDomainTemplate">
			<xsl:with-param name="colCount" select="5"/>
		</xsl:call-template>
		<!-- temporal information - assume dekad -->
		<xsl:call-template name="TemporalDomainTemplate">
			<xsl:with-param name="colCount" select="2"/>
		</xsl:call-template>
    <!-- distribution information-->
    <xsl:call-template name="DistributionTemplate">
      <xsl:with-param name="colCount" select="2"/>
    </xsl:call-template>
    <!-- quality information -->
    <xsl:call-template name="DataQualityTemplate">
    </xsl:call-template>
	</xsl:template>
  
	<!-- Content  tables creation -->
	<xsl:template match="gmd:contentInfo">
		<!-- image description information -->
		<xsl:call-template name="ContentTemplate">
             </xsl:call-template>
	</xsl:template>

  <!-- Ariticial last part tables creation starting from distributionInfo -->
  <xsl:template match="gmd:distributionInfo">
    <!-- point of contact description information -->
    <xsl:call-template name="PoCTemplate">
    </xsl:call-template>
    <!-- data policies information-->
    <xsl:call-template name="PoliciesTemplate">
      <xsl:with-param name="colCount" select="2"/>
    </xsl:call-template>
    <!-- extra information-->
    <xsl:call-template name="ExtraInfoTemplate">
    </xsl:call-template>    
  </xsl:template>
  
	<!-- Quality  tables creation -->
	<xsl:template match="dataQualityInfo">
		<!-- image description information -->
		<xsl:call-template name="DataQualityTemplate">
             </xsl:call-template>
	</xsl:template>
  
	<!-- Descriptor table template; mandatory -->
	<xsl:template name="DescriptionTemplate">
		<h2 style="margin-bottom: 0;">
			<a name="ProductInfo"/>
			<strong>Product Information</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">
				<tr>
					<xsl:for-each select="gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title">
						<th>
							<strong>Name</strong>
						</th>
						<td>
							<b>
								<span style="background-color:aquamarine">
									<xsl:value-of select="gco:CharacterString"/>
								</span>
							</b>
						</td>
					</xsl:for-each>
				</tr>
				<tr>
					<xsl:for-each select="gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:edition">
						<th>
							<strong>Version</strong>
						</th>
						<td>
							<b>
								<xsl:value-of select="gco:CharacterString"/>
							</b>
						</td>
					</xsl:for-each>
				</tr>
				<tr>
					<xsl:for-each select="gmd:MD_DataIdentification/gmd:abstract">
						<th width="200">
							<strong>Abstract</strong>
						</th>
						<td width="800">
							<xsl:value-of select="gco:CharacterString"/>
						</td>
					</xsl:for-each>
				</tr>
				<tr>
					<!-- need to navigate up from identificationInfo -->
					<xsl:for-each select="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage">
						<th width="200">Algorithm</th>
						<td width="800">
							<xsl:value-of select="gmd:statement/gco:CharacterString"/>
						</td>
				</xsl:for-each>
				</tr>
				<tr>
					<xsl:for-each select="gmd:MD_DataIdentification/gmd:purpose">
						<th width="200">
							<strong>Purpose</strong>
						</th>
						<td width="800">
							<xsl:value-of select="gco:CharacterString"/>
						</td>
					</xsl:for-each>
				</tr>
				<xsl:if test="gmd:MD_DataIdentification/gmd:descriptiveKeywords">
					<tr>
						<th>
							<strong>Keywords</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword">
								<xsl:value-of select="gco:CharacterString"/>;
						</xsl:for-each>
						</td>
					</tr>
				</xsl:if>
				<xsl:if test="gmd:MD_DataIdentification/gmd:topicCategory">
					<tr>
						<th>
							<strong>Keyword Categories</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:topicCategory">
								<xsl:value-of select="gmd:MD_TopicCategoryCode"/>;
						</xsl:for-each>
						</td>
					</tr>
				</xsl:if>
				<tr>
						<th>
							<strong>Platform</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:aggregationInfo/gmd:MD_AggregateInformation/gmd:initiativeType">
                <xsl:if test="gmd:DS_InitiativeTypeCode/attribute::codeListValue = 'platform'">
                  <xsl:value-of select="gmd:DS_InitiativeTypeCode"/>
                </xsl:if>
							</xsl:for-each>
						</td>
				</tr>
				<tr>
						<th>
							<strong>Sensor</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:aggregationInfo/gmd:MD_AggregateInformation/gmd:initiativeType">
                <xsl:if test="gmd:DS_InitiativeTypeCode/attribute::codeListValue = 'sensor'">
								<xsl:value-of select="gmd:DS_InitiativeTypeCode"/>
                </xsl:if>
							</xsl:for-each>
						</td>
				</tr>
				<tr>
						<th>
							<strong>Production Center</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty">
                <xsl:if test="gmd:role/gmd:CI_RoleCode = 'originator'">
                  <xsl:value-of select="gmd:organisationName/gco:CharacterString"/>
                </xsl:if>
							</xsl:for-each>
						</td>
				</tr>
				<tr>
						<th>
							<strong>Production Date</strong>
						</th>
						<td>
							<xsl:for-each select="../gmd:dateStamp">
                  <xsl:value-of select="gco:Date"/>
							</xsl:for-each>
						</td>
				</tr>
				<tr>
						<th>
							<strong>Production ID</strong>
						</th>
						<td>
							<xsl:for-each select="../gmd:fileIdentifier">
                  <xsl:value-of select="gco:CharacterString"/>
							</xsl:for-each>
						</td>
				</tr>
				<tr>
						<th>
							<strong>Status</strong>
						</th>
						<td>
							<xsl:for-each select="gmd:MD_DataIdentification/gmd:status">
								<xsl:value-of select="gmd:MD_ProgressCode"/>
							</xsl:for-each>
						</td>
				</tr>
			</table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>

	<!-- Spatial attributes table; mandatory -->
	<xsl:template name="SpatialDomainTemplate">
		<xsl:param name="colCount"/>
		<h2 style="margin-bottom: 0;">
			<a name="SpatialInfo"/>
			<strong>Spatial Information</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">
        <xsl:if test="../gmd:referenceSystemInfo">
          <tr>
            <th width="200">Projection</th>
            <td colspan="2">
	       <xsl:for-each select="../gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier">
	          <xsl:choose>
		      <xsl:when test="gmd:code/gco:CharacterString = 'WGS84'">
		      </xsl:when>
		      <xsl:otherwise>
                            <xsl:value-of select="gmd:code/gco:CharacterString"/>
	              </xsl:otherwise>
                  </xsl:choose>
              </xsl:for-each>
            </td>
          </tr>
          <tr>
            <th>Ellipsoid</th>
            <td colspan="2">
              <xsl:for-each select="../gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier">
                <xsl:if test="gmd:code/gco:CharacterString = 'WGS84'">
                  <xsl:value-of select="gmd:code/gco:CharacterString"/>
                </xsl:if>
              </xsl:for-each>
            </td>
          </tr>
        </xsl:if>
        <xsl:if test="gmd:MD_DataIdentification/gmd:spatialResolution/gmd:MD_Resolution/gmd:distance">
          <tr>
            <th>Resolution</th>
            <td colspan="2">
              <xsl:value-of select="gmd:MD_DataIdentification/gmd:spatialResolution/gmd:MD_Resolution/gmd:distance/gco:Distance"/>
            </td>
            <td colspan="2">degrees</td>
          </tr>
        </xsl:if>
        <xsl:if test="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/attribute::shortid">
          <tr>
            <th>Tile</th>
            <td>
              <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/attribute::shortid"/>
            </td>
          </tr>
        </xsl:if>
        <xsl:if test="../gmd:spatialRepresentationInfo">
          <tr>
            <th>Number of Lines</th>
            <td>
              <xsl:for-each select="../gmd:spatialRepresentationInfo/gmd:MD_Georectified/gmd:axisDimensionProperties/gmd:MD_Dimension">
                <xsl:if test="gmd:dimensionName/gmd:MD_DimensionNameTypeCode = 'row'">
                  <xsl:value-of select="gmd:dimensionSize/gco:Integer"/>
                </xsl:if>
              </xsl:for-each>
            </td>
          </tr>
          <tr>
            <th>Number of Columns</th>
            <td>
              <xsl:for-each select="../gmd:spatialRepresentationInfo/gmd:MD_Georectified/gmd:axisDimensionProperties/gmd:MD_Dimension">
                <xsl:if test="gmd:dimensionName/gmd:MD_DimensionNameTypeCode = 'column'">
                  <xsl:value-of select="gmd:dimensionSize/gco:Integer"/>
                </xsl:if>
              </xsl:for-each>
            </td>
          </tr>
        </xsl:if>        
				<xsl:variable name="colSpan" select="$colCount - 1"/>
				<xsl:if test="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement">
					<xsl:element name="th">
						<xsl:attribute name="colspan"><xsl:copy-of select="$colCount"/></xsl:attribute>
					</xsl:element>
					<xsl:if test="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox">
						<tr>
							<th rowspan="2">Bounding Rectangle</th>
							<th>North</th>
							<th>South</th>
							<th>West</th>
							<th>East</th>
						</tr>
						<tr>
              <td>
                <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal"/>
              </td>
              <td>
                <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal"/>
              </td>
							<td>
								<xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal"/>
							</td>
							<td>
								<xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal"/>
							</td>
						</tr>
					</xsl:if>
				</xsl:if>
        <xsl:if test="../gmd:spatialRepresentationInfo">
          <tr>
            <th>Corner point</th>
            <td>
              <xsl:value-of select="../gmd:spatialRepresentationInfo/gmd:MD_Georectified/gmd:cornerPoints/gml:Point/gml:name"/>
            </td>
          </tr>
          <tr>
            <th>Reference</th>
            <td>
              <xsl:value-of select="../gmd:spatialRepresentationInfo/gmd:MD_Georectified/gmd:pointInPixel/gmd:MD_PixelOrientationCode"/>
              of pixel
            </td>
          </tr>
        </xsl:if>
      </table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>

	<!-- Temporal attributes table; mandatory -->
	<xsl:template name="TemporalDomainTemplate">
		<xsl:param name="colCount"/>
		<h2 style="margin-bottom: 0;">
			<a name="TemporalInfo"/>
			<strong>Temporal Information</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">
					<xsl:if test="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent">
              <tr>
                <th width="200">Description</th>
                <td>
                  <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:description"/>
                </td>
              </tr>
              <tr>
                <th>Start date</th>
                <td>
                  <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition"/>
                </td>
              </tr>
              <tr>
                <th>End date</th>
                <td>
                  <xsl:value-of select="gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition"/>
                </td>
              </tr>
					</xsl:if>
			</table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>

  <!-- Distribution table; mandatory -->
  <xsl:template name="DistributionTemplate">
    <h2 style="margin-bottom: 0;">
      <a name="DistributionInfo"/>
      <strong>Distribution Information</strong>
    </h2>
    <blockquote style="margin-top: 0;">
      <table width="800" border="1">
        <tr>
        <th width="200">Product format</th>
          <td>
        <xsl:value-of select="gmd:MD_DataIdentification/gmd:resourceFormat/gmd:MD_Format/gmd:name/gco:CharacterString"/>
          <xsl:value-of select="gmd:MD_DataIdentification/gmd:resourceFormat/gmd:MD_Format/gmd:version/gco:CharacterString"/>
          </td>
        </tr>
        <tr>
        <th>Distribution format</th>
          <td>
            <xsl:value-of select="../gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name/gco:CharacterString"/>
            <xsl:value-of select="../gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:version/gco:CharacterString"/>
          </td>
        </tr>
      </table>
    </blockquote>
    <a href="#Top">back to top</a>
  </xsl:template>

	<!-- Quality table; optional -->
	<xsl:template name="DataQualityTemplate">
    <xsl:if test="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report">
		<h2 style="margin-bottom: 0;">
			<a name="ProductQuality"/>
			<strong>Product Quality</strong>
		</h2>
		<blockquote style="margin-top: 0;">
      <table width="800" border="1">

	<!-- Debricated /gmd:DQ_ThematicAccuracy, uses gmd:DQ_NonQuantitativeAttributeAccuracy or gmd:DQ_QuantitativeAttributeAccuracy instead -->      
        <xsl:for-each select="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_ThematicAccuracy/gmd:result">
          <tr>
            <th width="200">Thematic Accuracy</th>
	        <td>
		  <xsl:value-of select="gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
                </td>
            </tr>
          <tr>
	    <th width="200"></th>
	        <td>
		  <a>
                <xsl:attribute name="href">
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		</xsl:attribute>
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		  </a>
                </td>
            </tr>
    </xsl:for-each>

        <xsl:for-each select="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_NonQuantitativeAttributeAccuracy/gmd:result">
          <tr>
            <th width="200">Thematic Accuracy</th>
	        <td>
		  <xsl:value-of select="gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
                </td>
            </tr>
          <tr>
	    <th width="200"></th>
	        <td>
		  <a>
                <xsl:attribute name="href">
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		</xsl:attribute>
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		  </a>
                </td>
            </tr>
    </xsl:for-each>

        <xsl:for-each select="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_QuantitativeAttributeAccuracy/gmd:result">
          <tr>
            <th width="200">Thematic Accuracy</th>
	        <td>
		  <xsl:value-of select="gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
                </td>
            </tr>
          <tr>
	    <th width="200"></th>
	        <td>
		  <a>
                <xsl:attribute name="href">
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		</xsl:attribute>
			<xsl:value-of select="gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString"/>
		  </a>
                </td>
            </tr>
    </xsl:for-each>

        <xsl:for-each select="../gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result">
          <tr>
            <th width="200">Conformance</th>
	        <td>
		  <xsl:value-of select="gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
                </td>
            </tr>
        </xsl:for-each>

      </table>
		</blockquote>
		<a href="#Top">back to top</a>
    </xsl:if>
	</xsl:template>

	<!-- Data Policies; mandatory -->
	<xsl:template name="PoliciesTemplate">
		<h2 style="margin-bottom: 0;">
			<a name="DataPolicies"/>
			<strong>Data Policies</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">
        <xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:credit">
          <tr>
            <xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:credit">
              <th width="200">
                <strong>Credits</strong>
              </th>
              <td width="800">
                <xsl:value-of select="gco:CharacterString"/>
              </td>
            </xsl:for-each>
          </tr>
        </xsl:if>
	<xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useConstraints">
	  <tr>
		<th>
		<strong>Copyright</strong>
		</th>
		<td>
		<xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useConstraints">
			<xsl:value-of select="gmd:MD_RestrictionCode"/>
		</xsl:for-each>
		</td>
		</tr>
	</xsl:if>
        <xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints">
          <tr>
            <th>
              <strong>Access Constraints</strong>
            </th>
            <td>
              <xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints">
                <xsl:value-of select="gmd:MD_RestrictionCode"/>
              </xsl:for-each>
            </td>
          </tr>
        </xsl:if>
        <xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_Constraints/gmd:useLimitation">
          <tr>
            <th>
              <strong>Use Limitations</strong>
            </th>
            <td>
              <xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_Constraints/gmd:useLimitation">
                <xsl:value-of select="gco:CharacterString"/>
              </xsl:for-each>
            </td>
          </tr>
        </xsl:if>
			</table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>

	<!-- Documents and Quicklook; mandatory -->
	<xsl:template name="ExtraInfoTemplate">
		<h2 style="margin-bottom: 0;">
			<a name="ExtraInfo"/>
			<strong>Additional Information</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">

				<xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:graphicOverview">
					<tr>
						<th width="200">
							<strong>Quicklook</strong>
						</th>
						<td width="800">
							<a>
								<xsl:attribute name="href">
									<xsl:value-of select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:graphicOverview/gmd:MD_BrowseGraphic/gmd:fileName"/>
								</xsl:attribute>
								<xsl:value-of select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:graphicOverview/gmd:MD_BrowseGraphic/gmd:fileName"/>
							</a>
							<!-- old values
						      <a href=".">
						      <xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:graphicOverview/gmd:MD_BrowseGraphic/gmd:fileName">
								<xsl:value-of select="gco:CharacterString"/>
							</xsl:for-each>
						      </a>
						      -->
						</td>
					</tr>
				</xsl:if>
				<xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:otherCitationDetails">
					<tr>
						<th>
							<strong>Product User Manual</strong>
						</th>
            <td>
              <a>
                <xsl:attribute name="href">
                  <xsl:value-of select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:otherCitationDetails/gco:CharacterString"/>
                  </xsl:attribute>
                  <xsl:value-of select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:otherCitationDetails/gco:CharacterString"/>
              </a> 
						</td>
					</tr>
				</xsl:if>
				<xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:supplementalInformation">
					<tr>
						<th>
							<strong>Format Conversion Tool</strong>
						</th>
            <td>
              <a>
                <xsl:attribute name="href">
                  <xsl:value-of select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:supplementalInformation/gco:CharacterString"/>
                  </xsl:attribute>
                  VGTExtract
              </a> 
						</td>
					</tr>
				</xsl:if>
			</table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>

	<!-- Images  table -->
	<xsl:template name="ContentTemplate">
      <blockquote style="margin-top: 0;">
        <table width="800" border="1">
          <xsl:for-each select="gmd:MD_CoverageDescription">
            <tr>
              <th>
                <strong>
                  <span style="color:##00028B">
                    <xsl:value-of select="gmd:attributeDescription/gco:RecordType"/>
                  </span>
                </strong>
              </th>
            </tr>
            <!-- add here more image values -->
            <tr>
              <th>
                <i>Description</i>
              </th>
              <th>
                <i>minValue</i>
              </th>
              <th>
                <i>maxValue</i>
              </th>
              <th>
                <i>Scale</i>
              </th>
              <th>
                <i>Offset</i>
              </th>
              <th>
                <i>#bits</i>
              </th>
            </tr>

            <xsl:for-each select="gmd:dimension/gmd:MD_Band">
              <!-- filter out Display value -->
              <xsl:if test="not(gmd:sequenceIdentifier/gco:MemberName/gco:aName/gco:CharacterString = 'Display')">
                <tr>
                  <td>
                    <xsl:value-of select="gmd:sequenceIdentifier/gco:MemberName/gco:aName/gco:CharacterString"/>
                  </td>
                  <td>
                    <xsl:value-of select="gmd:minValue/gco:Real"/>
                  </td>
                  <td>
                    <xsl:value-of select="gmd:maxValue/gco:Real"/>
                  </td>
                  <td>
                    <xsl:value-of select="gmd:scaleFactor/gco:Real"/>
                  </td>
                  <td>
                    <xsl:value-of select="gmd:offset/gco:Real"/>
                  </td>
                  <td>
                    <xsl:value-of select="gmd:bitsPerValue/gco:Integer"/>
                  </td>
                </tr>
              </xsl:if>
            </xsl:for-each>
          </xsl:for-each>
        </table>
        <xsl:if test="gmd:MD_CoverageDescription">
          More information can be found in the Product User Manual
        </xsl:if>
      </blockquote>
	</xsl:template>

	<!-- Point of Contact  table -->
	<xsl:template name="PoCTemplate">
		<h2 style="margin-bottom: 0;">
			<a name="Contacts"/>
			<strong>Contacts</strong>
		</h2>
		<blockquote style="margin-top: 0;">
			<table width="800" border="1">
				<xsl:if test="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact">
					<xsl:for-each select="../gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty">
					<tr>
              	<th width="200" rowspan="3">
		    <xsl:if test="gmd:role/gmd:CI_RoleCode = 'owner'">
                        <strong>Owner Contact</strong>
		</xsl:if>
		    <xsl:if test="gmd:role/gmd:CI_RoleCode = 'custodian'">
                        <strong>Accountable Contact</strong>
		    </xsl:if>
                    <xsl:if test="gmd:role/gmd:CI_RoleCode = 'originator'">
                        <strong>Production Contact</strong>
                    </xsl:if>
                    <xsl:if test="gmd:role/gmd:CI_RoleCode = 'principalInvestigator'">
                        <strong>Scientific Contact</strong>
		    </xsl:if>
                </th>
						</tr>
						<tr>
							<td width="800">
								<xsl:value-of select="gmd:organisationName/gco:CharacterString"/>
							</td>
						</tr>
						<tr>
							<td width="800">
								<xsl:value-of select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString"/>
							</td>
						</tr>
					</xsl:for-each>
				</xsl:if>
        <xsl:if test="gmd:MD_Distribution/gmd:distributor">
          <xsl:for-each select="gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty">
            <tr>
              <th width="200" rowspan="3">
                <xsl:if test="gmd:role/gmd:CI_RoleCode = 'distributor'">
                  <strong>Distribution Contact</strong>
                </xsl:if>
              </th>
            </tr>
            <tr>
              <td width="800">
                <xsl:value-of select="gmd:organisationName/gco:CharacterString"/>
              </td>
            </tr>
            <tr>
              <td width="800">
                <xsl:value-of select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString"/>
              </td>
            </tr>
          </xsl:for-each>
        </xsl:if>
			</table>
		</blockquote>
		<a href="#Top">back to top</a>
	</xsl:template>
</xsl:stylesheet>
