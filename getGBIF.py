#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:57:55 2020

@author: vincenzomadaghiele
"""

import requests
import pandas as pd

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

#set parameters for API call
params = ['limit=300', 'hasCoordinate=true', 'hasGeospatialIssue=false', 'speciesKey=9055455'] #This SpeciesKey is for camel
#Set up a simple while loop to continue downloading until the last #page
df = pd.DataFrame()
endOfRecords = False
offset = 0
status = 200

while endOfRecords == False and status == 200:
    df, endOfRecords, status = get_GBIF_response(base_url, offset, params, df)
    offset = len(df) + 1
    