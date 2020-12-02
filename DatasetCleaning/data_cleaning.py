import os
import sys
import cdsapi
import netCDF4 as nc
import numpy as np
import xarray as xa
import pandas as pd
import glob
import matplotlib.pyplot as plt
from scipy import stats

# If one module is missing, add it to modules_path
dataset_path = os.path.abspath(os.path.join(__file__, '..', '..', 'Dataset'))
current_path = os.path.abspath(os.path.join(__file__, '..'))
modules_path = [dataset_path, current_path]
for path in modules_path:
    if path not in sys.path:
        sys.path.append(path)

from areas import regions
import dataset_api as api
import utils as ut

folder = os.path.abspath(os.path.join(__file__, '..'))
action = 'mean'
handle = 'custom_set'

for r in regions:
    region = regions[r]
    lat = region['latitude']
    lon = region['longitude']
    area = [lat[1], lon[0], lat[0], lon[1]]

    
    # CLIMATE
    ## Set this flag to get the average of 2012 or to pass the 
    ##same year/month of the land dataset
    
    get_average_year = True
    
    if(get_average_year):
        climate_path = folder + '/climate/' + r + '_2012avg_climate.nc'
        df_cds = ut.get_climate_dataset(climate_path, area)
    else:
        year = region['year']
        month = region['month']
        climate_path = folder + '/' + r + '_' + str(year) + '_' + str(month) + 'avg_climate.nc'
        df_cds = ut.get_climate_dataset(climate_path, area, year)
    
    
    print("Climate\t" + r + "\tnull data count: ", df_cds.isna().any().sum())
    
    df_cds = df_cds.groupby(['longitude', 'latitude']).mean()
    
    
    # LAND
    land_path = folder + '/land/' + r + "_land.csv"
    df_land = ut.get_land_dataset(land_path, lat, lon)
    print("Land\t" + r + " \tnull data count: ", df_cds.isna().any().sum())
    
    # ADD RICHNESS
    richness_path = folder + "/richness/EEA_richness_latLon_" + r + ".csv"
    
    df_richness = pd.read_csv(richness_path).drop(columns=['Unnamed: 0'])

    df_richness = df_richness.loc[(df_richness['latitude'] >= lat[0]) & (df_richness['latitude'] <= lat[1]) 
                            & (df_richness['longitude'] >= lon[0]) & (df_richness['longitude'] <= lon[1])]
    
    df_richness = df_richness[df_richness.habitat_richness > 0]
    df_richness.set_index(['longitude', 'latitude'], inplace=True)
    
    df_richness_land = df_richness.merge(df_land, left_index=True, right_index=True)
    
    # FILTER LAND
    

    df_richness_land = ut.land_handle_specific_values(df_richness_land, handle=handle)

    df_richness_land = ut.handle_outliers(df=df_richness_land, columns=ut.albedo_labels + ut.tocr_labels, area=area, action=action, verbose=True)
    
    df_richness_land = ut.handle_outliers(df=df_richness_land, columns=ut.swi_labels, area=area, detect='no_detection', action=action, verbose=True)
    
    
    # MERGE WITH CLIMATE
    
    df_final = ut.merge_climate_land(df_cds, df_richness_land)
    
    
    ## SAVE
    if(get_average_year):
        merge_name = r + '_yearavg_out_' + action + '_handle_' + handle + '.csv'
    else:
        merge_name = r + '_out_' + action + '_handle_' + handle + '.csv'
        
    merge_path = os.path.abspath(os.path.join(__file__, '..', '..', 'Dataset', merge_name))
    
    df_final.to_csv(merge_path)