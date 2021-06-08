<h1>GIS_Python_Scripts</h1>
<p>Scripts I've made to do various little things in GIS using either OSGEO libraries or arcpy.  All scripts generally written for Python 3.x</p>

<h2>create_rectangle.py</h2>
<p>Sometimes you just need to create a rectangle with a specific aspect ratio.  This script will do that given the upper left XY coordinate of that rectangle, the aspect ratio, the length (in map units) of the shortest side of the rectangle, your spatial reference, and whether your want it in landscape or portrait orientation.</p>
<p>Writes out a shapefile with the rectangle.</p>
<p> Weird things probably happen, depending on which projection you're using, if you are doing this over a Rather Large Area...</p>
<p>Requires osgeo module:  https://anaconda.org/conda-forge/gdal</p>

<h2>scale_features.py</h2>
<p> A simple script using the <a href="https://pypi.org/project/Fiona/" target="_blank">Fiona</a> and <a href="https://pypi.org/project/Shapely/" target="_blank">Shapely</a> libraries to uniformly scale features using an affine transformation </p>
