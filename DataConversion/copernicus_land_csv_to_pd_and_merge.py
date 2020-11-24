#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:55:38 2020

@author: vincenzomadaghiele

@description: This script takes a list of Copernicus Land GeoTiff files 
    and corresponding csv (conversion from geoTiff to csv is handled 
    in the script 'geoTiff_to_csv_copernicus_land.py'). 
    It opens the scripts as pandas dataframes and merges them into coordinates 
    sampled with 0.01 precision

Things to do:
    - identify categorical variables
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
land_data.rename(columns = {'x':'longitude','y': 'latitude','z':'NDVI'}, inplace = True)
# Cut latitude and longitude
land_data['latitude'] = land_data.apply(cutLat, axis=1)
land_data['longitude'] = land_data.apply(cutLon, axis=1)
land_data = land_data.groupby(['latitude','longitude'])['NDVI'].mean().reset_index()


#%%

path  = 'data/copernicus_land_france/'
datasets = ['ALBH1k', 'ALDH1k', 'BA300', 'DMP300', 'FAPAR300', 'FCOVER300', 'GDMP300', 
            'HLST1k', 'LAI300', 'SSM1k', 'SWI1k', 'TOCR1k', 'VCI']

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
        
        print('-'*30)
        print('Loading: ' + var_name)
        print('-'*30)
        
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
        DATA.rename(columns = {'x':'longitude','y': 'latitude','z':var_name}, inplace = True)
        # cut latitude and longitude
        DATA['latitude'] = DATA.apply(cutLat, axis=1)
        DATA['longitude'] = DATA.apply(cutLon, axis=1)
        # make the mean of the values with the same (lat,lon) couple
        DATA = DATA.groupby(['latitude','longitude'])[var_name].mean().reset_index()
        # merge with general dataset
        land_data = land_data.merge(DATA,on=["latitude",'longitude'], how = "outer")
        i += 1

export_path = 'data/france_land.csv'
land_data.to_csv(export_path, index = True)

land_data_drop = land_data.drop(columns=['DMP300-RT0-QFLAG', 'GDMP300-RT0-QFLAG', 'FAPAR300-RT0-NOBS', 
                                'FAPAR300-RT0-LENGTH-AFTER','FAPAR300-RT0-QFLAG', 'FAPAR300-RT0-RMSE',
                               'FAPAR300-RT0-LENGTH-BEFORE', 'FCOVER300-RT0-QFLAG','FCOVER300-RT0-LENGTH-AFTER',
                                'FCOVER300-RT0-NOBS', 'FCOVER300-RT0-LENGTH-BEFORE','FCOVER300-RT0-RMSE', 
                               'LAI300-RT0-LENGTH-BEFORE','LAI300-RT0-LENGTH-AFTER', 'LAI300-RT0-NOBS',
                                'LAI300-RT0-RMSE', 'LAI300-RT0-QFLAG','SWI1km-QFLAG-015', 'SWI1km-QFLAG-020',
                                'SWI1km-QFLAG-060', 'SWI1km-QFLAG-010', 'SWI1km-SSF',
                                'SWI1km-QFLAG-005', 'SWI1km-QFLAG-100', 'SWI1km-QFLAG-040',
                                'SWI1km-QFLAG-002', 'SSM1km-ssm-noise', 'LST-Q-FLAGS', 
                                'LST-PERCENT-PROC-PIXELS', 'LST-ERRORBAR-LST','LST-TIME-DELTA',
                               'ALDH-AL-DH-QFLAG', 'ALDH-NMOD', 'ALDH-LMK', 'ALDH-AL-DH-BB-ERR',
                                'ALDH-AL-DH-VI-ERR', 'ALDH-AL-DH-NI-ERR', 'ALBH-LMK',
                                'ALBH-NMOD', 'ALBH-AL-BH-QFLAG','ALBH-AL-BH-BB-ERR', 
                                'ALBH-AL-BH-VI-ERR', 'ALBH-AL-BH-NI-ERR', 
                               'TOCR-TOCR-QFLAG', 'TOCR-NMOD','TOCR-REF-NOR-SWIR-ERR', 
                                'TOCR-REF-NOR-RED-ERR','TOCR-REF-NOR-BLUE-ERR', 'TOCR-SZN',
                                'TOCR-REF-NOR-NIR-ERR', 'BA300-FDOB-DEKAD', 'BA300-BA-DEKAD',
                                'BA300-FDOB-SEASON', 'BA300-CP-DEKAD'])

export_path = 'data/france_land_drop.csv'
land_data_drop.to_csv(export_path, index = True)