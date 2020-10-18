# GIS_Python_Scripts
Scripts I've made to do various little things in GIS using either OSGEO libraries or arcpy.  All scripts generally written for Python 3.x

<b>create_rectangle.py</b>
Sometimes you just need to create a rectangle with a specific aspect ratio.  This script will do that given the upper left XY coordinate of that rectangle, the aspect ratio, the length (in map units) of the shortest side of the rectangle, your spatial reference, and whether your want it in landscape or portrait orientation.

Writes out a shapefile with the rectangle.

Requires osgeo module:  https://anaconda.org/conda-forge/gdal
