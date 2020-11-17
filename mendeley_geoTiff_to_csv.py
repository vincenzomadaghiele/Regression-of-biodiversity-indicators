#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:51:02 2020

@author: vincenzomadaghiele

@dependencies: 
    - GDAL (conda install gdal)
    - rasterio (pip install rasterio)
    - raster2xyz (pip install raster2xyz)
    
@description: this script reads mendeley geoTiff files and 
    converts them to csv
"""

# Read a geotiff
# Convert to csv
# Read the csv to pandas
# filter only france values
# cut coordinates
# merge to the general dataset with new column
# count the ones and the zeros for each coordinate


# geoTiff libraries
import rasterio as rs
from rasterio.plot import show
from raster2xyz.raster2xyz import Raster2xyz
# general purpose
import glob


# Instanciate Raster2xyz()
rtxyz = Raster2xyz()

path = 'data/mendeley_modeling/2650133/spdist_thrsld.tif'

out_path = 'spdist_thrsld.csv'
print('----------------')
print('Converting: ')
print('----------------')
rtxyz.translate(path, out_path)
# plot dataset
dataset = rs.open(path)
show(dataset)
# Print specifications
print('No. of bands' + str(dataset.count))
print('Image resolution: ' + str(dataset.height) + str(dataset.width))
print('Coordinate Reference System (CRS): ' + str(dataset.crs))



'''
path  = 'data/mendeley_modeling/*'
plants_paths = glob.glob(path)
for plant in plants_paths:
    tiff_file = 'spdist_thrsld.tif'


# names of the geoTiff and csv dataset folders
datasets = ['ALBH1k', 'ALDH1k', 'BA300', 'DMP300', 'FAPAR300', 'FCOVER300', 'GDMP300', 
            'HLST1k', 'LAI300', 'NDVI300', 'SSM1k', 'SWI1k', 'TOCR1k', 'VCI']

i = 0
for dataset in datasets: 
    
    tiff_path = path + dataset + '/*.tiff'
    csv_path = path + dataset
    tiff_files = glob.glob(tiff_path)
    
    for i in range(len(tiff_files)):
    
        #file_name = tiff_files[i][31:-5] # solve this name issue
        
        # Name of the file without .tiff extension
        file_name = tiff_files[i].split('/')[-1][:-5]
        out_path = csv_path + '/' + file_name + '.csv'
        
        print('----------------')
        print('Converting: ' + file_name)
        print('----------------')
        
        rtxyz.translate(tiff_files[i], out_path)
        # plot dataset
        rsFile = rs.open(tiff_files[i])
        show(rsFile)
        # Print specifications
        print('No. of bands' + str(rsFile.count))
        print('Image resolution: ' + str(rsFile.height) + str(rsFile.width))
        print('Coordinate Reference System (CRS): ' + str(rsFile.crs))

'''