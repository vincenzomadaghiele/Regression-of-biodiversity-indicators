#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:28:42 2020

@author: vincenzomadaghiele
"""

# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
from raster2xyz.raster2xyz import Raster2xyz
# general purpose
import glob


# Instanciate Raster2xyz()
rtxyz = Raster2xyz()

# convert teh EEA geoTiff to csv
source_path = 'data/eea_r_3035_1_km_forest-assemblage-sps_2006.tif'
csv_path = 'data/'

file_name = source_path[5:-4]
out_path = csv_path + file_name + '.csv'
print('----------------')
print('Converting: ' + file_name)
print('----------------')
rtxyz.translate(source_path, out_path)
# plot dataset
dataset = rs.open(source_path)
show(dataset)
# Print specifications
print('No. of bands' + str(dataset.count))
print('Image resolution: ' + str(dataset.height) + str(dataset.width))
print('Coordinate Reference System (CRS): ' + str(dataset.crs))

