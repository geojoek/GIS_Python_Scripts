# Script for scaling a feature in a shapefile and writing out to a new shapefile
# Note, this needs to be run in a virtual environment, Python 3.7.7 or slightly earlier,
# with fiona and shapely libaries, and their dependencies, installed. Or else Bad Things Happen
# Script by Joe Kopera, June 2021

# Inspiration / help:
# https://gis.stackexchange.com/questions/52705/how-to-write-shapely-geometries-to-shapefiles
# https://shapely.readthedocs.io/en/stable/manual.html#shapely.affinity.scale
# Script modeled after: https://github.com/Toblerity/Fiona/blob/master/examples/with-shapely.py


import logging
import sys

from shapely.geometry import shape, mapping
from shapely import affinity

import fiona

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# Parameters
input_file = r"FILENAMEANDPATH"
output_file = input_file.rstrip(".shp") + "_scaled.shp"
scale_factor = 1.3

# opens input file for reading into a fiona "collection" object (object type: dictionary)
with fiona.open(input_file, "r") as input:

    # Opens output file for writing
    # **source.meta is a shortcut to get the crs, driver, and schema
    # keyword arguments from the source feature "Collection" / file.
    with fiona.open(output_file, "w", **input.meta) as output:

        # We iterate through all the features in the feature "collection" (dictionary) fiona
        # created by opening the input file above on line 21
        for feature in input:
            try:
                geom = shape(feature["geometry"])
                assert geom.is_valid
                scaled_shape = affinity.scale(geom, xfact=scale_factor, yfact=scale_factor, origin="center")
                assert scaled_shape.is_valid

                # Writes the output file
                # The output feature object is a dictionary, and to copy the properties of that feature
                # we just copy the dictionary key.  Easy peasy! ugh.
                output.write({
                    "geometry": mapping(scaled_shape),
                    "properties": feature["properties"]
                })
            except:
                logging.exception("Error reading feature %s", feature['id'])