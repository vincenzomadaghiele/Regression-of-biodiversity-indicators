#!/usr/bin/env python
import cdsapi
    
def get_era5_land(store_path, area, year):
    c = cdsapi.Client()

    c.retrieve(
    'reanalysis-era5-land-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '2m_dewpoint_temperature', '2m_temperature', 'forecast_albedo',
            'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'skin_reservoir_content',
            'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2',
            'soil_temperature_level_3', 'soil_temperature_level_4', 'surface_latent_heat_flux',
            'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_pressure',
            'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'total_precipitation',
            'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3',
            'volumetric_soil_water_layer_4',
        ],
        'year': year,
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': '00:00',
        'area': area,
        'format': 'netcdf',
    },
    store_path)

