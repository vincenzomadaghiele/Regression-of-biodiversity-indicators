#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:22:40 2020

@author: vincenzomadaghiele
@dependencies: 
    - GDAL (conda install gdal)
    - rasterio (pip install rasterio)
    - raster2xyz (pip install raster2xyz)
@description: this script reads geoTiff file and converts it to csv
"""

# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
from raster2xyz.raster2xyz import Raster2xyz
# general purpose
import glob


# Instanciate Raster2xyz()
rtxyz = Raster2xyz()


#%% convert to csv all the geoTiff files in species_count
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


#%% convert to csv all the geoTiff files in species_count
source_path = 'data/spdist_thrsld1.tif'
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

#%%

import pandas as pd
# load NDVI300 csv as pandas dataframe
csv = 'data/spdist_thrsld1.csv'
df = pd.read_csv(csv)
# latitude : x, longitude : y, value : z
df.rename(columns = {'x':'longitude','y':'latitude','z':'value'}, inplace = True)

#%%
df_france1 = df.loc[df['latitude'] >= 3.5].loc[df['latitude'] <= 4.6].loc[df['longitude'] >= 44.3].loc[ df['longitude'] <= 45]


#%% convert to csv all the geoTiff files in species_count
source_path = 'data/spdist_thrsld2.tif'
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

#%%

# load NDVI300 csv as pandas dataframe
csv = 'data/spdist_thrsld2.csv'
df = pd.read_csv(csv)
# latitude : x, longitude : y, value : z
df.rename(columns = {'x':'longitude','y':'latitude','z':'value'}, inplace = True)

#%%
df_france2 = df.loc[df['latitude'] >= 3.5].loc[df['latitude'] <= 4.6].loc[df['longitude'] >= 44.3].loc[ df['longitude'] <= 45]


'''
#%% convert to csv all the geoTiff files in NDVI300
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


#%% convert to csv all the geoTiff files in LAI300
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
    # plot dataset
    dataset = rs.open(source_files[i])
    show(dataset)
    # Print specifications
    print('No. of bands' + str(dataset.count))
    print('Image resolution: ' + str(dataset.height) + str(dataset.width))
    print('Coordinate Reference System (CRS): ' + str(dataset.crs))


#%% convert to csv all the geoTiff files in FCOVER300
source_path = 'data/copernicus_land/FCOVER300/*.tiff'
csv_path = 'data/copernicus_land/FCOVER300/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][31:-5]
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


#%% convert to csv all the geoTiff files in FPAR300
source_path = 'data/copernicus_land/FPAR300/*.tiff'
csv_path = 'data/copernicus_land/FPAR300/'
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


#%% convert to csv all the geoTiff files in DMP300
source_path = 'data/copernicus_land/DMP300/*.tiff'
csv_path = 'data/copernicus_land/DMP300/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][28:-5]
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


#%% convert to csv all the geoTiff files in SWI1k
source_path = 'data/copernicus_land/SWI1k/*.tiff'
csv_path = 'data/copernicus_land/SWI1k/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][27:-5]
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


#%% convert to csv all the geoTiff files in HLST1k
source_path = 'data/copernicus_land/HLST1k/*.tiff'
csv_path = 'data/copernicus_land/HLST1k/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][28:-5]
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


#%% convert to csv all the geoTiff files in ALDH1k
source_path = 'data/copernicus_land/ALDH1k/*.tiff'
csv_path = 'data/copernicus_land/ALDH1k/'
source_files = glob.glob(source_path)

for i in range(len(source_files)):
    file_name = source_files[i][28:-5]
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

'''
