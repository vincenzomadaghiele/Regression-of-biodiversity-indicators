# Regression of species richness biodiversity indicator from satellite observations and environmental parameters
##### Authors: Vincenzo Madaghiele, Cosimo Chetta
##### Supervisor: Maria A. Zuluaga

###### This project was developed for the MALIS course at EURECOM university. It received an honorable mention among many projects in the course from a jury of researchers and industry professionals: https://malis-course.github.io/2020/11/22/final-projects/

## Project Description

Measuring biodiversity is often a complex and resource demanding task, which requires observations on the field. The European Union’s satellite infrastructure provides a constant stream of data, which is already used for different ecological monitoring applications. This experiment focuses on measuring the species richness biodiversity indicator from satellite observations and environmental parameters only, in order to provide a scalable, habitat-level method for biodiversity measuring. After building an appropriate database by collecting and aggregating different environmental variables, we have focused on comparing the performances of different regression models on the data, then we have experimented with a more complex neural network architecture, including satellite images into the datasets.

<img src="https://github.com/vincenzomadaghiele/Regression-of-biodiversity-indicators/blob/master/TreeVisualization/imgs/Italy_example.png" alt="italy_example" width="800"/>

###### A closer description of the project can be found in the [project report](https://github.com/vincenzomadaghiele/Regression-of-biodiversity-indicators/blob/master/Documents/MALIS_project_final_report.pdf) and in the [presentation slides](https://github.com/vincenzomadaghiele/Regression-of-biodiversity-indicators/blob/master/Documents/MALIS%20project%20slides.pdf)

## Running the code

The libraries necessary to running this code are listed in the requirement.txt file. 
After downloading this repository, run the following code in the terminal to install the dependencies:
```
conda env create -f gdal-env.yml
conda activate gdal_env
```

## Code description

* Data Conversion : code used for data format conversion 
* Dataset : datasets of the different areas used for training 
* DatasetCleaning : code used to pre-process the datasets
* Documents : documents related to the project
* Regression : code for regression model run and comparison
* TreeVisualization : code for feature importances and tree visualization
