#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:00:03 2021

@author: vincenzomadaghiele
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import geopandas

path = "data/italy_out_closest_point_mean_handle_custom_set.csv"
df = pd.read_csv(path)
#df = df.sort_values('y')
#df = df.drop(columns="geometry")
df.head()
plot_true = df[['latitude','longitude','habitat_richness']]


# Visualiza true dataset
gdf = geopandas.GeoDataFrame(plot_true, geometry=geopandas.points_from_xy(plot_true.longitude, plot_true.latitude), 
                            crs="EPSG:4326")
print(gdf.head())
gdf.plot(markersize=.1, 
         figsize=(8, 8),
         column = 'habitat_richness',
        legend = True, 
        cmap = 'YlOrRd',
        legend_kwds={'label': "Species richness", 
         'shrink': 0.5})


#%% Compute regression

regression_label = 'habitat_richness'

it = pd.read_csv(path, index_col=['longitude', 'latitude'])
#it = it.sort_index(ascending=True)
y = it[regression_label].values
X = it.drop(columns=[regression_label]).values #returns a numpy array

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, shuffle=True)

# Normalize the data
X_scaler = preprocessing.MinMaxScaler()
y_scaler = preprocessing.MinMaxScaler()

# Test values have to be normalized with the training mean and std
y_scaler.fit(y_train.reshape(-1, 1))
y_train = y_scaler.transform(y_train.reshape(-1, 1)).ravel()
y_test = y_scaler.transform(y_test.reshape(-1, 1)).ravel()
y = y_scaler.transform(y.reshape(-1, 1)).ravel()
X_scaler.fit(X_train)
X_train = X_scaler.transform(X_train)
X_test = X_scaler.transform(X_test)
X = X_scaler.transform(X)

rfr_it = RandomForestRegressor(n_estimators=100, max_depth=None)
rfr_it = rfr_it.fit(X_train,y_train)
print("Random Forest validation score: ", rfr_it.score(X_test, y_test))


#%% Spatialize regression results
# WARNING: slow!

it_drop = it.drop(columns=[regression_label])
predicted = []
for i, row in it_drop.iterrows():
    #y_row = it[regression_label].values
    x_row = row.values #returns a numpy array
    #print(x_row)
    # normalize it
    x_row = X_scaler.transform(x_row.reshape(1, -1))
    # predict it
    y_pred = rfr_it.predict(x_row)
    # un-normalize it
    y_unnormalized = y_scaler.inverse_transform(y_pred.reshape(1, -1))
    #row['richness_prediction'] = y_unnormalized
    predicted.append([i[0], i[1], y_unnormalized[0][0], it.loc[(i[0], i[1])]['habitat_richness'], abs(y_unnormalized[0][0] - it.loc[(i[0], i[1])]['habitat_richness'])])
    # add it to the dataset

pred_df = pd.DataFrame(predicted,columns=['longitude','latitude','predicted_richness','real_richness','difference'])
# Visualiza predicted dataset
gdf_pred = geopandas.GeoDataFrame(pred_df, 
                            geometry=geopandas.points_from_xy(pred_df.longitude, pred_df.latitude), 
                            crs="EPSG:4326")

#%% Visualize regression

print(gdf_pred.head())
gdf_pred.plot(markersize=.1, 
         figsize=(8, 8),
         column = 'predicted_richness',
        legend = True, 
        cmap = 'YlOrRd',
        legend_kwds={'label': "Predicted richness", 
         'shrink': 0.5})

    

