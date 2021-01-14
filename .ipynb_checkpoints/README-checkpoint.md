# Regression of species richness biodiversity indicator from satellite observations and environmental parameters
##### Authors: Vincenzo Madaghiele, Cosimo Chetta

## Project Description

Measuring biodiversity is often a complex and resource demanding task, which requires observations on the field. The European Union’s satellite infrastructure provides a constant stream of data, which is already used for different ecological monitoring applications. This experiment focuses on measuring the species richness biodiversity indicator from satellite observations and environmental parameters only, in order to provide a scalable, habitat-level method for biodiversity measuring. After building an appropriate database by collecting and aggregating different environmental variables, we have focused on comparing the performances of different regression models on the data, then we have experimented with a more complex neural network architecture, including satellite images into the datasets.

## Running the code

The libraries necessary to running this code are listed in the requirement.txt file. 
After downloading this repository, it is necessary to run the following code in the terminal:
```
$ conda create --name <env> --file requirements.txt
```

## Code description

* Data Conversion : code used for data format conversion 
* Dataset : datasets of the different areas used for training 
* DatasetCleaning : code used to pre-process the datasets
* Documents : documents related to the project
* Regression : code for regression model run and comparison
* TreeVisualization : code for feature importances and tree visualization