#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:02:17 2020

@author: vincenzomadaghiele

@description: this scripts takes a GBIF occurrencies csv database 
    and process the rows in order to obtain the number of species 
    for each 0.01 square in the dataset. The obtained dataset is 
    saved as csv and merged with France Copernicus Land data.
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

GBIF_csv_path = 'data/GBIF_france.csv'
GBIF_france = pd.read_csv(GBIF_csv_path, error_bad_lines=False, sep='\t')

#%% cut the columns 'decimalLatitude' and 'decimalLongitude' to 0.01 precision
# count unique species (.groupBy(['lat','lon'])['species'].nunique())
# create dataset with only 'lat', 'lon', 'num_species'
# export to csv the first one and the second one

def cutLat(row):
    return int(row['decimalLatitude']*100)/100
def cutLon(row):
    return int(row['decimalLongitude']*100)/100


GBIF_france['decimalLatitude'] = GBIF_france.apply(cutLat, axis=1)
GBIF_france['decimalLongitude'] = GBIF_france.apply(cutLon, axis=1)

export_path = 'data/GBIF_france_cutLatLon.csv'
GBIF_france.to_csv(export_path, index = True)

unique_species_count = GBIF_france.groupby(['decimalLatitude','decimalLongitude'])['speciesKey'].nunique().reset_index()

export_path = 'data/GBIF_france_unique_species_count.csv'
unique_species_count.to_csv(export_path, index = True)


#%% Merge GBIF with France Copernicus Land data

france_land_path = 'data/france_land.csv'
france_land = pd.read_csv(france_land_path)

unique_species_count.rename(columns = {'decimalLatitude':'latitude', 'decimalLongitude':'longitude'}, inplace = True) 

land_GBIF = france_land.merge(unique_species_count,on=["latitude",'longitude'])

