# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:02:17 2021


"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
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
mp = Basemap(projection = 'merc', 
             llcrnrlon = 0,
             llcrnrlat = 90, 
             urcrnrlon = 357.5,
             urcrnrlat = -90,
             resolution= 'i')

# To see the shape of the variable SLP, in Console (Spyder) we can type the following commands
# slp.shape
#lat.shape
#lon.shape
#time.shape
