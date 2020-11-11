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

land_data['latitude'] = land_data.apply(cutLat, axis=1)
land_data['longitude'] = land_data.apply(cutLon, axis=1)

#%%

'''
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

# Scale values 0-255 --> 0-7 (correct FCOVER interval)
def scaleFCOVER(row):
    return (row['FCOVER']/255)*1
# apply function
FCOVER['FCOVER'] = FCOVER.apply(scaleFCOVER, axis=1)

FCOVER['latitude'] = FCOVER.apply(cutLat, axis=1)
FCOVER['longitude'] = FCOVER.apply(cutLon, axis=1)

land_data = land_data.merge(FCOVER,on=["latitude",'longitude'])
'''

#%%

path  = 'data/copernicus_land/'
datasets = ['DMP300', 'FPAR300']

i = 0
for dataset in datasets: 
    
    tiff_path = path + dataset + '/*.tiff'
    csv_path = path + dataset + '/*.csv'
    tiff_files = glob.glob(tiff_path)
    csv_files = glob.glob(csv_path)
    
    for i in range(len(tiff_files)):
    
        #var_name = tiff_files[i][31:-5] # solve this name issue
        # This naming should be universal for all files and make each variable unique
        var_name = tiff_files[i].split('/')[-1].split('.')[0][6:]
        
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
        # cut latitude and longitude
        DATA['latitude'] = DATA.apply(cutLat, axis=1)
        DATA['longitude'] = DATA.apply(cutLon, axis=1)
        # merge with general dataset
        land_data = land_data.merge(DATA,on=["latitude",'longitude'])
        i += 1
