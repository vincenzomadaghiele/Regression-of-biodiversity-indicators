#!/usr/bin/env python

import math
import pandas as pd
import numpy as np

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
        if(math.isnan(data.loc[d])):
            values = [standard_value] * 4
            for j, direction in enumerate(directions):
                lon, lat = d
                x_off, y_off = direction
                off = 0
                while((lon, lat) in data.index):
                    if(math.isnan(data.loc[(lon, lat)]) == False):
                        values[j] = data.loc[(lon, lat)]
                        break
                    off += 1
                    lon += x_off*precision*off
                    lat += y_off*precision*off
            data.loc[d] = np.mean(values)
    return data