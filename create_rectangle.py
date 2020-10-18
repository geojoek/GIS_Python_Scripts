# PURPOSE: To create a shapefile with a single rectangle polygon of a certain aspect ratio via concatening WKT for that polygon
# There are probably more efficient ways to do this that don't involve WKT
# You may still have to re-scale the rectangle in your GIS desktop app to fit, but at least it will have proper aspect ratio
# Assumes you are within a UTM coordinate system to the northeast of the origin

# Script by Joe Kopera, October 2020

# DEPENDENCIES: Should be run in conda environment with Python 3.x and osgeo & gdal libraries installed

# TRIVIA: I initially used the regex (re) module to extract coordinates from the input XY coordinates
# ... but then it occured to me it's simpler and more pythonic to just treat the coordinate pair as a list.

import osgeo.ogr as ogr
import osgeo.osr as osr

# Parameters:
upperLeft_XY_Input = [208443,4698424] # Upper left XY coordinate of polygon you want to crate. These should be in the units defined by your spatial reference / EPSG
aspectRatio = "1.5"
orientation = "landscape" # either "landscape" or "portrait"
lengthShortSide = "1000" # again, should be in units defined by your spatial reference
epsg = int("26919") # the EPSG code of your spatial reference
outputSHP = r"/your/output/path" # where you would like the script to write out your shapefile

# ----------------

# calculating extent of rectangle polygon based on parameters above
minX = str(upperLeft_XY_Input[0])
maxY = str(upperLeft_XY_Input[1])

if orientation == "landscape":
    minY = str(float(upperLeft_XY_Input[1]) - float(lengthShortSide))
    maxX = str(float(upperLeft_XY_Input[0]) + (float(aspectRatio) * float(lengthShortSide)))
else:
    minY = str(float(upperLeft_XY_Input[1]) - (float(aspectRatio) * float(lengthShortSide)))
    maxX = str(float(upperLeft_XY_Input[0]) + float(lengthShortSide))

# Concatenating WKT for polygon coordinates
polygonWKT = "POLYGON((" + minX + " " + maxY + "," + maxX + " " + maxY + "," + maxX + " " + minY + "," + minX + " " + minY + "," + minX + " " + maxY + "))"

print("Polygon extent in WKT is:\n{}".format(polygonWKT))

# write out a shapefile for the polygon to save time loading the WKT and doing a "Save As" in QGIS
# I stole a lot of this and heavily modified it from https://gis.stackexchange.com/questions/354016/create-an-esri-shapefile-from-wkt-with-ogr

driver = ogr.GetDriverByName("ESRI Shapefile") # set up the shapefile driver
data_source = driver.CreateDataSource(outputSHP) # create the data source

# create the spatial reference
srs = osr.SpatialReference()
srs.ImportFromEPSG(epsg)

# create the layer
layer = data_source.CreateLayer("output", srs, ogr.wkbPolygon)

# create the feature
feature = ogr.Feature(layer.GetLayerDefn())

# create the WKT for the feature using Python string formatting
polygon = ogr.CreateGeometryFromWkt(polygonWKT)

# Set the feature geometry using the point
feature.SetGeometry(polygon)

# Create the feature in the layer (shapefile)
layer.CreateFeature(feature)

# Clean up and shut down
feature = None # Dereference the feature
data_source = None # Save and close the data source

print("Written out shapefile to {}".format(outputSHP))