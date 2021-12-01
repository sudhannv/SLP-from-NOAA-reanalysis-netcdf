# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:02:17 2021

@author: Sidharth-Sasi
"""

from netCDF4 import Dataset
import numpy as np
# import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
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
mp = Basemap(projection = 'merc', 
             llcrnrlon = 0,
             llcrnrlat = 90, 
             urcrnrlon = 357.5,
             urcrnrlat = -90,
             resolution= 'i')