#!/usr/bin/env python
import cdsapi

def get_era5_pressure():
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-pressure-levels-monthly-means',
        {
            'format': 'netcdf',
            'product_type': 'monthly_averaged_reanalysis',
            'variable': [
                'specific_humidity', 'specific_rain_water_content', 'temperature',
            ],
            'pressure_level': [
                '1', '2', '3',
                '5', '7', '10',
                '20', '30', '50',
                '70', '100', '125',
                '150', '175', '200',
                '225', '250', '300',
                '350', '400', '450',
                '500', '550', '600',
                '650', '700', '750',
                '775', '800', '825',
                '850', '875', '900',
                '925', '950', '975',
                '1000',
            ],
            'year': '2019',
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'time': '00:00',
            'area': [
                70, 10, 35,
                30,
            ],
        },
        'ERA5_pressure.nc')
    
def get_era5_land():
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-land-monthly-means',
        {
            'product_type': 'monthly_averaged_reanalysis',
            'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                '2m_temperature', 'forecast_albedo', 'leaf_area_index_high_vegetation',
                'leaf_area_index_low_vegetation', 'skin_reservoir_content', 'skin_temperature',
                'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3',
                'soil_temperature_level_4', 'surface_latent_heat_flux', 'surface_net_solar_radiation',
                'surface_net_thermal_radiation', 'surface_pressure', 'surface_sensible_heat_flux',
                'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'total_precipitation',
                'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4',
            ],
            'year': '2019',
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'time': '00:00',
            'area': [
                70, 10, 35,
                30,
            ],
            'format': 'netcdf',
        },
        'ERA5_land.nc')

def get_era5_data():
    
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'format': 'netcdf',
            'product_type': 'monthly_averaged_reanalysis',
            'variable': [
                '2m_dewpoint_temperature', '2m_temperature', 'high_vegetation_cover',
                'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'low_vegetation_cover',
                'mean_evaporation_rate', 'mean_surface_latent_heat_flux', 'mean_total_precipitation_rate',
                'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2',
                'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type',
                'surface_net_solar_radiation', 'surface_pressure', 'surface_solar_radiation_downwards',
                'total_cloud_cover', 'type_of_high_vegetation', 'type_of_low_vegetation',
                'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4',
            ],
            'year': '2019',
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'time': '00:00',
            'area': [
                70, 10, 35,
                30,
            ],
        },
        'ERA5_data.nc')