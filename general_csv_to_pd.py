#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:18:45 2020

@author: vincenzomadaghiele
@dependencies: 
    - pyproj (conda install pyproj)
    - GDAL (conda install gdal)
    - rasterio (pip install rasterio)
@description: this script reads a geoTiff file 
    and the corresponding csv as pandas dataframe
"""

# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
# general purpose
import pandas as pd

# Show the NDVI geoTiff
NDVItiff = 'data/copernicus_land/NDVI300/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.tiff'
NDVIrs = rs.open(NDVItiff)
show(NDVIrs)
# Print specifications of NDVI geoTiff
# Print specifications
print('No. of bands' + str(NDVIrs.count))
print('Image resolution: ' + str(NDVIrs.height) + str(NDVIrs.width))
print('Coordinate Reference System (CRS): ' + str(NDVIrs.crs))

# load NDVI300 csv as pandas dataframe
NDVIcsv = 'data/copernicus_land/NDVI300/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.csv'
NDVI = pd.read_csv(NDVIcsv)
# latitude : x, longitude : y, value : z
NDVI.rename(columns = {'x':'latitude','y':'longitude','z':'NDVI'}, inplace = True)

# Scale values 0-255 --> 0-9 (correct LAI interval)
# Scaling is just for consistency, as data will be normalized anyway 
# so it will not matter
def scaleNDVI(row):
    return (row['NDVI']/255)*9
# apply function
NDVI['NDVI'] = NDVI.apply(scaleNDVI, axis=1)
