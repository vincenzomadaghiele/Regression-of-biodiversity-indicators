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


# Instanciate Raster2xyz()
rtxyz = Raster2xyz()


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



