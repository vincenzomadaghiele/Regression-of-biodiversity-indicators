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

for region in regions:
    
    lat = regions[region]['latitude']
    lon = regions[region]['longitude']
    area = [lat[1], lon[0], lat[0], lon[1]]

    
    # CLIMATE
    climate_path = folder + '/' + region + '_climate.nc'
    df_cds = ut.get_climate_dataset(climate_path, area, regions[region]['year'])
    print("Climate\t" + region + "\tnull data count: ", df_cds.isna().any().sum())
    
    df_cds = df_cds.groupby(['longitude', 'latitude']).mean()
    
    
    # LAND
    land_path = folder + '/' + region + "_land.csv"
    df_land = ut.get_land_dataset(land_path, lat, lon)
    print("Land\t" + region + " \tnull data count: ", df_cds.isna().any().sum())

    df_land = ut.land_handle_specific_values(df_land)

    df_land = ut.handle_outliers(df=df_land, columns=ut.albedo_labels + ut.tocr_labels, area=area, action='closest_point_mean', verbose=False)
    df_land = ut.handle_outliers(df=df_land, columns=ut.swi_labels, area=area, detect='no_detection', action='closest_point_mean', verbose=False)

    # MERGE LAND AND CLIMATE
    
    df_cds_land = ut.merge_climate_land(df_cds, df_land)
    
    # ADD RICHNESS
    richness_path = folder + "/EEA_richness_latLon_" + region + ".csv"
    
    df_richness = pd.read_csv(richness_path).drop(columns=['Unnamed: 0'])

    df_richness = df_richness.loc[(df_richness['latitude'] >= lat[0]) & (df_richness['latitude'] <= lat[1]) 
                            & (df_richness['longitude'] >= lon[0]) & (df_richness['longitude'] <= lon[1])]
    
    df_richness = df_richness[df_richness.habitat_richness > 0]
    df_richness.set_index(['longitude', 'latitude'], inplace=True)
    
    df_final = df_richness.merge(df_cds_land, left_index=True, right_index=True)
    
    ## SAVE
    merge_name = 'france.csv'
    merge_path = os.path.abspath(os.path.join(__file__, '..', '..', 'Dataset', merge_name))
    
    df_final.to_csv(merge_path)