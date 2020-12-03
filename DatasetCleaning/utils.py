#!/usr/bin/env python

import math
import pandas as pd
import numpy as np
import dataset_api as api
import xarray as xa
import os
from scipy import stats

albedo_labels = ['ALBH-AL-BH-NI', 'ALBH-AL-BH-VI', 'ALBH-AL-BH-BB',
                 'ALDH-AL-DH-BB', 'ALDH-AL-DH-VI', 'ALDH-AL-DH-NI']
tocr_labels = ['TOCR-REF-NOR-BLUE', 'TOCR-REF-NOR-NIR', 'TOCR-REF-NOR-SWIR', 'TOCR-REF-NOR-RED']
swi_labels = ['SWI1km-SWI-002', 'SWI1km-SWI-100', 'SWI1km-SWI-040', 'SWI1km-SWI-005', 
              'SWI1km-SWI-010', 'SWI1km-SWI-060', 'SWI1km-SWI-015', 'SWI1km-SWI-020']

def get_climate_dataset(path, area, year=2012, 
                        month=['01', '02', '03',
                            '04', '05', '06',
                            '07', '08', '09',
                            '10', '11', '12']):
    '''
    If exists, return the climate dataset of an area, 
    otherwise retrieve it from cds api and store it in
    path
    
    Parameters
    ----------
    
    path: path of the dataset
    area: coordinates of the area
    year: year to retrieve
    
    Return
    ------
    df: dataframe of climate dataset
    
    '''
    
    if not os.path.isfile(path):
        api.get_era5_land(path, area, year, month)
        
    with xa.open_mfdataset(path) as ds:
        df_cds = ds.to_dataframe() 
    return df_cds

def get_land_dataset(path, lat, lon):
    '''

    Parameters
    ----------
    path : path of the csv
    lat : array with boundary latitudes 
    lon : array with boundary longitudes

    Returns
    -------
    df_land : dataframe of land dataset

    '''
    df_land = pd.read_csv(path)
    
    # Retrieving only data of our location
    df_land = df_land.loc[(df_land['latitude'] >= lat[0]) & (df_land['latitude'] <= lat[1]) 
                            & (df_land['longitude'] >= lon[0]) & (df_land['longitude'] <= lon[1])]
    
    df_land = df_land.set_index(['longitude', 'latitude'])
    #df_land.index = df_land.index.map(lambda index: (int(index[0]*100), int(index[1]*100)))
    
    # Manually excluding features
    df_land = df_land.drop(columns=['DMP300-RT0-QFLAG', 'GDMP300-RT0-QFLAG', 'FAPAR300-RT0-NOBS', 
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
                                    'BA300-FDOB-SEASON', 'BA300-CP-DEKAD', 'SSM1km-ssm', 
                                    'Unnamed: 0', 'LST-LST' ], errors='ignore')
    
    ############################################################
    # TEMPORARY REMOVING THOSE COLUMNS FOR ERRORS IN THE DATASET
    ############################################################
    df_land = df_land.drop(columns=['VCI_x', 'VCI_y'])
    
    return df_land

def land_handle_specific_values(df_land, handle='custom_set'):
    '''
    handle specific values specified in the documentation, such
    as errors or data too high/low

    Parameters
    ----------
    df_land : dataframe of land dataset
    handle : how to handle the specific values
        'custom_set' = custom handling based on documentation
        'set_null' = set values to None

    Returns
    -------
    df_land

    '''
    
    handle_types = ['custom_set', 'set_null']
    
    if(handle not in handle_types):
        print('handle type not valid, please specify an handle from ', handle_types)
        return df_land
        
    df_albedo = df_land[albedo_labels].copy()
    df_tocr = df_land[tocr_labels].copy()
    df_swi = df_land[swi_labels].copy()
    
    albedo_specific_min = df_albedo[df_albedo == 65534]
    albedo_specific_max = df_albedo[df_albedo > 10000]
    tocr_specific = df_tocr[df_tocr > 2400]
    swi_specific_error = df_swi[df_swi >= 252]
    swi_specific_greater = df_swi[df_swi > 200]
    
    if(handle == 'custom_set'):
        df_albedo[np.isfinite(albedo_specific_max)] = 10000
        df_albedo[np.isfinite(albedo_specific_min)] = 0
        df_tocr[np.isfinite(tocr_specific)] = None
        df_swi[np.isfinite(swi_specific_greater)] = 200
        df_swi[np.isfinite(swi_specific_error)] = None
        
        
    if(handle == 'set_null'):
        df_albedo[np.isfinite(albedo_specific_max)] = None
        df_albedo[np.isfinite(albedo_specific_min)] = None
        df_tocr[np.isfinite(tocr_specific)] = None
        df_swi[np.isfinite(swi_specific_greater)] = None
        df_swi[np.isfinite(swi_specific_error)] = None
    
    df_land[albedo_labels] = df_albedo
    df_land[tocr_labels] = df_tocr
    df_land[swi_labels] = df_swi
    
    return df_land

def handle_outliers(df, columns, area, detect='z_score', action='closest_point_mean', verbose=False):
    '''
    

    Parameters
    ----------
    df_land : dataframe
    columns : columns on which perform outliers detection
    detect : technique to detect the outliers
        'z_score': set as outliers values with z_score > 3,
        'no_detection': do not detected outiers, used to handle previous null values
    action : operation to handle outliers
        'closest_point_mean': perform the mean of the 4 closest point for each direction, 
        'mean': mean of the column, 
        'remove': remove the rows with null values

    Returns
    -------
    df_land 

    '''
    
    def z_score(df):
        # Return boolean mask with outliers set to true 
        return (np.abs(stats.zscore(df)) > 3)
    
    def no_detection(df):
        # Used to perform only the fill of missing values
        return np.full(df.shape, False)
    
    def closest_point_mean(df, df_outliers, cols, area):
        # Fill null values with average of closest point 
        for col in cols:
            df_outliers[col] = mean_of_closest_point(df_outliers[col], 0.01, area, df_outliers[col].mean())
        df[cols] = df_outliers
        return df
    
    def mean(df, df_outliers, cols, area):
        df[cols] = df_outliers.fillna(df_outliers.mean())
        return df
    
    def remove(df, df_outliers, cols, area):
        df[cols] = df_outliers
        return df.dropna(subset=cols)
                    
    detections = {'z_score': z_score, 'no_detection': no_detection}
    actions = {'closest_point_mean': closest_point_mean, 'mean': mean, 'remove': remove}
    
    if(detect not in detections):
        print("Specify a correct detection.")
        return
    if(action not in actions):
        print("Specify a correct action.")
        return
    
    df_outliers = df[columns].copy()
    mask = detections[detect](df_outliers)
    
    if(verbose):
        print("Found " + str(mask.sum()) + " outliers")
        
    df_outliers[mask] = None
    
    if(verbose):
        print("Number of null values to handle per columns: ")
        print(df_outliers.isna().sum())
    
    df = actions[action](df, df_outliers, columns, area)
    
    return df   

def merge_climate_land(df_cds, df_land):
    '''

    Parameters
    ----------
    df_cds : climate dataframe
    df_land : land dataframe

    Returns
    -------
    df : merged cds, land dataframe

    '''
    
    def distance(lon1, lon2, lat1, lat2):
        return np.sqrt((lon1-lon2)**2 + (lat1-lat2)**2)

    df1 = df_cds.reset_index()
    df2 = df_land.reset_index()
    
    minimum = [-1] * df2.shape[0]
    coords_y = df1.values[:, 0:2]
    for i, [lon_x, lat_x] in enumerate(df2.values[:, 0:2]):
        distances = list(map(lambda coord_y: distance(lon_x, coord_y[0], lat_x, coord_y[1]), coords_y))
        minimum[i] = np.argmin(distances)
    
    df1.drop(columns=['longitude', 'latitude'], inplace=True)
    df2['merge_index'] = minimum
    df = df2.merge(df1, left_on='merge_index', right_index=True).drop(columns=['merge_index'])
    df.set_index(['longitude', 'latitude'], inplace=True)
    return df

def mean_of_closest_point(data, precision, margin, standard_value=0):
    '''
    For each null value in data perform an average of the
    4 not null closest points in an Longitude-Latitude
    indexed pandas
    
    Parameters
    ----------
    
    data: array containing some null values
    precision: step length of the research
    
    Return
    ------
    
    new_data: data with no null values
    
    '''    
    
    directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    
    i = precision
    for d in data.index:
        if(math.isnan(data.loc[d].values[0])):
            values = [standard_value] * 4
            for j, direction in enumerate(directions):
                lon, lat = d
                x_off, y_off = direction
                off = 0
                while((lon, lat) in data.index):
                    if(math.isnan(data.loc[(lon, lat)].values[0]) == False):
                        values[j] = data.loc[(lon, lat)].values[0]
                        break
                    off += 1
                    lon += x_off*precision*off
                    lat += y_off*precision*off
            data.loc[d].values[0] = np.mean(values)
    return data