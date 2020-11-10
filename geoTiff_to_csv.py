#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:22:40 2020

@author: vincenzomadaghiele
@dependencies: 
    - GDAL (conda install gdal)
    - rasterio (pip install rasterio)
    - raster2xyz (pip install raster2xyz)
@description: this script reads Copernicus LAND geoTiff files and converts it to csv
"""

# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
from raster2xyz.raster2xyz import Raster2xyz
# general purpose
import glob

# NDVI index in geoTiff format (300 meters precision)
NDVItiff = 'data/copernicus_land/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.tiff'
dataset = rs.open(NDVItiff)
show(dataset)
# Print specifications
print(dataset.count)
print(dataset.height, dataset.width)
print(dataset.crs)

# convert NDIV300 to csv
file_name = NDVItiff[28:-5]
print('Converting: ' + file_name)
print('----------------')
out_csv = "data/copernicus_land/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.csv"
rtxyz = Raster2xyz()
rtxyz.translate(NDVItiff, out_csv)

# convert to csv all the geoTiff files in LAI300
source_path = 'data/copernicus_land/LAI300/*.tiff'
csv_path = 'data/copernicus_land/LAI300/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][28:-5]
    out_path = csv_path + file_name + '.csv'
    print('----------------')
    print('Converting: ' + file_name)
    print('----------------')
    rtxyz.translate(source_files[i], out_path)
