#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:18:45 2020

@author: vincenzomadaghiele
@dependencies: 
    - GDAL (conda install gdal)
    - rasterio (pip install rasterio)
@description: this script reads Copernicus LAND geoTiff files 
    and converted csv files and convert it to pandas dataframe
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


#%% Show the LAI geoTiff
LAItiff = 'data/copernicus_land/LAI300/c_gls_LAI300-RT0-LAI_202010310000_CUSTOM_OLCI_V1.1.1.tiff'
LAIrs = rs.open(LAItiff)
show(LAIrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(LAIrs.count))
print('Image resolution: ' + str(LAIrs.height) + str(LAIrs.width))
print('Coordinate Reference System (CRS): ' + str(LAIrs.crs))

# load LAI300 csv as pandas dataframe
LAIcsv = 'data/copernicus_land/LAI300/c_gls_LAI300-RT0-LAI_202010310000_CUSTOM_OLCI_V1.1.1.csv'
LAI = pd.read_csv(LAIcsv)
# latitude : x, longitude : y, value : z
LAI.rename(columns = {'x':'latitude','y':'longitude','z':'LAI'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct LAI interval)
def scaleLAI(row):
    return (row['LAI']/255)*7
# apply function
LAI['LAI'] = LAI.apply(scaleLAI, axis=1)


#%% Show the FCOVER geoTiff
FCOVERtiff = 'data/copernicus_land/FCOVER300/c_gls_FCOVER300-RT0-FCOVER_202010310000_CUSTOM_OLCI_V1.1.1.tiff'
FCOVERrs = rs.open(FCOVERtiff)
show(FCOVERrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(FCOVERrs.count))
print('Image resolution: ' + str(FCOVERrs.height) + str(FCOVERrs.width))
print('Coordinate Reference System (CRS): ' + str(FCOVERrs.crs))

# load LAI300 csv as pandas dataframe
FCOVERcsv = 'data/copernicus_land/FCOVER300/c_gls_FCOVER300-RT0-FCOVER_202010310000_CUSTOM_OLCI_V1.1.1.csv'
FCOVER = pd.read_csv(FCOVERcsv)
# latitude : x, longitude : y, value : z
FCOVER.rename(columns = {'x':'latitude','y':'longitude','z':'FCOVER'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct LAI interval)
def scaleFCOVER(row):
    return (row['FCOVER']/255)*1
# apply function
FCOVER['FCOVER'] = FCOVER.apply(scaleFCOVER, axis=1)

