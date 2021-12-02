# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:02:17 2021

import datetime as dt
from netCDF4 import Dataset
import numpy as np
# import cartopy.crs as ccrs
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
# from matplotlib.cbook import dedent
import warnings
warnings.filterwarnings('ignore')
ncfile='slp.1970.nc'
print('Reading the nc file')
data=Dataset(ncfile)
lat=data.variables['lat'][:]
print('Extracting Latitutde')
lon=data.variables['lon'][:]
print('Extracting Longitude')
time=data.variables['time'][:]
print('Extracting Time')
slp=data.variables['slp'][:]
print('Extracting slp')
m = Basemap(projection = 'moll', 
             llcrnrlon = 0,
             llcrnrlat = -90, 
             urcrnrlon = 360,
             urcrnrlat = 90,
             resolution= 'i', lon_0=0)
m.drawcoastlines()
m.drawmapboundary()
        # To see the shape of the variable SLP, in Console (Spyder) we can type the following commands
        # slp.shape
        #lat.shape
        #lon.shape
        #time.shape
time_idx = 287  # for a day number 287 in data file
offset = dt.timedelta(hours=48)    
# List of all times in the file as datetime objects
dt_time = [dt.date(1, 1, 1) + dt.timedelta(hours=t) - offset\
           for t in time]
cur_time = dt_time[time_idx]
slp_cyclic, lon_cyclic = addcyclic(slp[time_idx, :, :], lon)
# Shift the grid so lons go from -180 to 180 instead of 0 to 360.
slp_cyclic, lon_cyclic = shiftgrid(180., slp_cyclic, lon_cyclic, start=False)
# Create 2D lat/lon arrays for Basemap
lon2d, lat2d = np.meshgrid(lon_cyclic, lat)
# Transforms lat/lon into plotting coordinates for projection
x, y = m(lon2d, lat2d)
# Plot of air temperature with 11 contour intervals
cs = m.contourf(x, y, slp_cyclic, 11, cmap=plt.cm.Spectral_r)
cbar = plt.colorbar(cs, orientation='horizontal', shrink=0.5)
cbar.set_label("%s (%s)" % (nc_fid.variables['slp'].var_desc,\
                            nc_fid.variables['slp'].units))
plt.title("%s on %s" % (nc_fid.variables['slp'].var_desc, cur_time))

