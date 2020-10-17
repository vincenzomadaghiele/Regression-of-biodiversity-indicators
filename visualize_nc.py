#from netCDF4 import Dataset  # use scipy instead
from scipy.io import netcdf #### <--- This is the library to import.

fp='c_gls_LAI-RT0_202006300000_GLOBE_PROBAV_V2.0.1.nc' # your file name with the eventual path
# Open file in a netCDF reader
directory = './'
wrf_file_name = fp
nc = netcdf.netcdf_file(wrf_file_name,'r')

#Look at the variables available
nc.variables

#Look at the dimensions
nc.dimensions

#Look at a specific variable's dimensions
nc.variables['T2'].dimensions   ## output is ('Time', 'south_north', 'west_east')

#Look at a specific variable's units
nc.variables['T2'].units        ## output is ('K')