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
NDVItiff = 'data/copernicus_land_france/NDVI300/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.tiff'
NDVIrs = rs.open(NDVItiff)
show(NDVIrs)
# Print specifications of NDVI geoTiff
# Print specifications
print('No. of bands' + str(NDVIrs.count))
print('Image resolution: ' + str(NDVIrs.height) + str(NDVIrs.width))
print('Coordinate Reference System (CRS): ' + str(NDVIrs.crs))

# load NDVI300 csv as pandas dataframe
NDVIcsv = 'data/copernicus_land_france/NDVI300/c_gls_NDVI300-NDVI_202010210000_CUSTOM_PROBAV_V1.0.1.csv'
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

land_data['latitude'] = land_data.apply(cutLat, axis=1)
land_data['longitude'] = land_data.apply(cutLon, axis=1)
land_data = land_data.groupby(['latitude','longitude'])['NDVI'].mean().reset_index()

#%%

path  = 'data/copernicus_land_france/'
datasets = ['ALBH1k', 'ALDH1k', 'BA300', 'DMP300', 'FAPAR300', 'FCOVER300', 'GDMP300', 
            'HLST1k', 'LAI300', 'NDVI300', 'SSM1k', 'SWI1k', 'TOCR1k', 'VCI']

i = 0
for dataset in datasets: 
    
    tiff_path = path + dataset + '/*.tiff'
    csv_path = path + dataset + '/*.csv'
    tiff_files = glob.glob(tiff_path)
    csv_files = glob.glob(csv_path)
    
    for i in range(len(tiff_files)):
    
        #var_name = tiff_files[i][31:-5] # solve this name issue
        # This naming should be universal for all files and make each variable unique
        var_name = tiff_files[i].split('/')[-1].split('.')[0].split('_')[2]
        
        print('-'*89)
        print('Loading: ' + var_name)
        print('-'*89)
        
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
        DATA.rename(columns = {'x':'latitude','y':'longitude','z':var_name}, inplace = True)
        # cut latitude and longitude
        DATA['latitude'] = DATA.apply(cutLat, axis=1)
        DATA['longitude'] = DATA.apply(cutLon, axis=1)
        # make the mean of the values with the same (lat,lon) couple
        DATA = DATA.groupby(['latitude','longitude'])[var_name].mean().reset_index()
        # merge with general dataset
        land_data = land_data.merge(DATA,on=["latitude",'longitude'])
        i += 1

export_path = 'data/france_land.csv'
land_data.to_csv(export_path, index = True)

