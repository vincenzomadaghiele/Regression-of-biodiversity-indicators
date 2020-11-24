#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:25:45 2020

@author: vincenzomadaghiele

@description: this script calls the GBIF API and retreives the data
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon


base_url = "https://api.gbif.org/v1/occurrence/search?"

def get_GBIF_response(base_url, offset, params, df):
    """Performs an API call to the base URL with additional parameters listed in 'params'. 
    Concatenates response to a Pandas DataFrame, 'df'."""
    
    #Construct the query URL
    query = base_url+'&'+f'offset={offset}'
    for each in params:
        query = query+'&'+each
    
    #Call API
    response = requests.get(query)
    
    #If call is successful, add data to df
    if response.status_code != 200:
        print(f"API call failed at offset {offset} with a status code of {response.status_code}.")
    else:
        result = response.json()
        df_concat = pd.concat([df, pd.DataFrame.from_dict(result['results'])], axis = 0, ignore_index = True, sort = True)
        endOfRecords = result['endOfRecords']
        return df_concat, endOfRecords, response.status_code


#%% Get the data from GBIF API


#set parameters for API call
#params = ['limit=300', 'hasCoordinate=true', 'hasGeospatialIssue=false', 'geometry='+polygon, ]

lat_range = '44.3,44.9'
lon_range = '3.6,4.6'
kingdom_key = '6' # kingdom: plantae
params = ['limit=300', 'hasCoordinate=true', 'hasGeospatialIssue=false', 
          'decimalLatitude='+lat_range, 'decimalLongitude='+lon_range, 'kingdomKey='+kingdom_key ]
#Set up a simple while loop to continue downloading until the last #page
df = pd.DataFrame()
endOfRecords = False
offset = 0
status = 200

while endOfRecords == False and status == 200:
    df, endOfRecords, status = get_GBIF_response(base_url, offset, params, df)
    offset = len(df) + 1
    
    
#%% cut the columns 'decimalLatitude' and 'decimalLongitude' to 0.01 precision
# count unique species (.groupBy(['lat','lon'])['species'].nunique())
# create dataset with only 'lat', 'lon', 'num_species'
# export to csv the first one and the second one
    
def cutLat(row):
    return int(row['decimalLatitude']*100)/100
def cutLon(row):
    return int(row['decimalLongitude']*100)/100

export_path = 'data/GBIF_france.csv'
df.to_csv(export_path, index = True)

df['decimalLatitude'] = df.apply(cutLat, axis=1)
df['decimalLongitude'] = df.apply(cutLon, axis=1)

export_path = 'data/GBIF_france_cutLatLon.csv'
df.to_csv(export_path, index = True)

unique_species_count = df.groupBy(['decimalLatitude','decimalLongitude'])['species'].nunique().reset_index()

export_path = 'data/GBIF_france_unique_species_count.csv'
df.to_csv(export_path, index = True)

