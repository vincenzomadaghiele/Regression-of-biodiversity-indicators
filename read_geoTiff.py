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

# Scale values 0-255 --> 0-7 (correct FCOVER interval)
def scaleFCOVER(row):
    return (row['FCOVER']/255)*1
# apply function
FCOVER['FCOVER'] = FCOVER.apply(scaleFCOVER, axis=1)


#%% Show the FPAR geoTiff
FPARtiff = 'data/copernicus_land/FPAR300/c_gls_FAPAR300-RT0-FAPAR_202010310000_CUSTOM_OLCI_V1.1.1.tiff'
FPARrs = rs.open(FPARtiff)
show(FPARrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(FPARrs.count))
print('Image resolution: ' + str(FPARrs.height) + str(FPARrs.width))
print('Coordinate Reference System (CRS): ' + str(FPARrs.crs))

# load LAI300 csv as pandas dataframe
FPARcsv = 'data/copernicus_land/FPAR300/c_gls_FAPAR300-RT0-FAPAR_202010310000_CUSTOM_OLCI_V1.1.1.csv'
FPAR = pd.read_csv(FPARcsv)
# latitude : x, longitude : y, value : z
FPAR.rename(columns = {'x':'latitude','y':'longitude','z':'FPAR'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct FPAR interval)
def scaleFPAR(row):
    return (row['FPAR']/255)*1
# apply function
FPAR['FPAR'] = FPAR.apply(scaleFPAR, axis=1)


#%% Show the DMP geoTiff
DMPtiff = 'data/copernicus_land/DMP300/c_gls_DMP300-RT0-DMP_202010310000_CUSTOM_OLCI_V1.1.1.tiff'
DMPrs = rs.open(DMPtiff)
show(DMPrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(DMPrs.count))
print('Image resolution: ' + str(DMPrs.height) + str(DMPrs.width))
print('Coordinate Reference System (CRS): ' + str(DMPrs.crs))

# load LAI300 csv as pandas dataframe
DMPcsv = 'data/copernicus_land/DMP300/c_gls_DMP300-RT0-DMP_202010310000_CUSTOM_OLCI_V1.1.1.csv'
DMP = pd.read_csv(DMPcsv)
# latitude : x, longitude : y, value : z
DMP.rename(columns = {'x':'latitude','y':'longitude','z':'DMP'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct DMP interval)
def scaleDMP(row):
    return (row['DMP']/255)*1
# apply function
DMP['DMP'] = DMP.apply(scaleDMP, axis=1)


#%% Show the SWI geoTiff
SWItiff = 'data/copernicus_land/SWI1k/c_gls_SWI1km-SWI-100_202011011200_CUSTOM_SCATSAR_V1.0.1.tiff'
SWIrs = rs.open(SWItiff)
show(SWIrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(SWIrs.count))
print('Image resolution: ' + str(SWIrs.height) + str(SWIrs.width))
print('Coordinate Reference System (CRS): ' + str(SWIrs.crs))

# load LAI300 csv as pandas dataframe
SWIcsv = 'data/copernicus_land/SWI1k/c_gls_SWI1km-SWI-100_202011011200_CUSTOM_SCATSAR_V1.0.1.csv'
SWI = pd.read_csv(SWIcsv)
# latitude : x, longitude : y, value : z
SWI.rename(columns = {'x':'latitude','y':'longitude','z':'SWI'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct DMP interval)
def scaleSWI(row):
    return (row['SWI']/255)*1
# apply function
SWI['SWI'] = SWI.apply(scaleSWI, axis=1)


#%% Show the ALDH1k geoTiff
ALDHtiff = 'data/copernicus_land/ALDH1k/c_gls_ALDH-NMOD_201912130000_CUSTOM_PROBAV_V1.5.1.tiff'
ALDHrs = rs.open(ALDHtiff)
show(ALDHrs)
# Print specifications of LAI geoTiff
# Print specifications
print('No. of bands' + str(ALDHrs.count))
print('Image resolution: ' + str(ALDHrs.height) + str(ALDHrs.width))
print('Coordinate Reference System (CRS): ' + str(ALDHrs.crs))

# load LAI300 csv as pandas dataframe
ALDHcsv = 'data/copernicus_land/ALDH1k/c_gls_ALDH-NMOD_201912130000_CUSTOM_PROBAV_V1.5.1.csv'
ALDH = pd.read_csv(ALDHcsv)
# latitude : x, longitude : y, value : z
ALDH.rename(columns = {'x':'latitude','y':'longitude','z':'ALDH'}, inplace = True)

# Scale values 0-255 --> 0-7 (correct DMP interval)
def scaleALDH(row):
    return (row['ALDH']/255)*1
# apply function
ALDH['ALDH'] = ALDH.apply(scaleALDH, axis=1)




