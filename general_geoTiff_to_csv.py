#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:30:24 2020

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

# convert to csv all the geoTiff files in NDVI300
source_path = 'data/copernicus_land/NDVI300/*.tiff'
csv_path = 'data/copernicus_land/NDVI300/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][29:-5]
    out_path = csv_path + file_name + '.csv'
    print('----------------')
    print('Converting: ' + file_name)
    print('----------------')
    rtxyz.translate(source_files[i], out_path)
    # plot dataset
    dataset = rs.open(source_files[i])
    show(dataset)
    # Print specifications
    print('No. of bands' + str(dataset.count))
    print('Image resolution: ' + str(dataset.height) + str(dataset.width))
    print('Coordinate Reference System (CRS): ' + str(dataset.crs))

