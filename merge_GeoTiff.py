#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:55:38 2020

@author: vincenzomadaghiele
"""

# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
# general purpose
import pandas as pd
import glob


def cutLat(row):
    return int(row['latitude']*100)/100
def cutLon(row):
    return int(row['longitude']*100)/100

# Read first dataset (NDVI300) in order to do the merge
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
land_data = pd.read_csv(NDVIcsv)
# latitude : x, longitude : y, value : z
land_data.rename(columns = {'x':'latitude','y':'longitude','z':'NDVI'}, inplace = True)

# Scale values 0-255 --> 0-9 (correct LAI interval)
# Scaling is just for consistency, as data will be normalized anyway 
# so it will not matter
def scaleNDVI(row):
    return (row['NDVI']/255)*9
# apply function
land_data['NDVI'] = land_data.apply(scaleNDVI, axis=1)

#%%

path  = 'data/copernicus_land/'
variables = ['FCOVER300']

i = 0
for var_name in variables: 
    
    tiff_path = path + var_name + '/*.tiff'
    csv_path = path + var_name + '/*.csv'
    tiff_files = glob.glob(tiff_path)
    csv_files = glob.glob(csv_path)
    
    for i in range(len(tiff_files)):
    
        var_name = tiff_files[i][28:-5]
        
        print('----------------')
        print('Loading: ' + var_name)
        print('----------------')
        
        # Show the dataset
        tiff = tiff_files[i]
        rsDATA = rs.open(tiff)
        show(rsDATA)
        # Print specifications
        print('No. of bands' + str(rsDATA.count))
        print('Image resolution: ' + str(rsDATA.height) + str(rsDATA.width))
        print('Coordinate Reference System (CRS): ' + str(rsDATA.crs))
        
        # load csv as pandas dataframe
        csv = csv_files[i]
        DATA = pd.read_csv(csv)
        # latitude : x, longitude : y, value : z
        DATA.rename(columns = {'x':'latitude','y':'longitude','z':'var'+str(i)}, inplace = True)
        # merge with general dataset
        DATA['latitude'] = DATA.apply(cutLat, axis=1)
        DATA['longitude'] = DATA.apply(cutLon, axis=1)
        
        land_data = land_data.merge(DATA,on=["latitude",'longitude'])
        i += 1
