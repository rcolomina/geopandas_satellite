# Run this with python3

import pandas as pd
import geopandas
import matplotlib.pyplot as plt



data_origin="./fast_output_extrations/"


df_lon = pd.read_csv(data_origin+"lon.txt")
df_lon.columns = ['lon']
df_lat = pd.read_csv(data_origin+"lat.txt")
df_lat.columns = ['lat']


print(df_lon.head())
print(df_lat.head())
df = pd.concat((df_lat,df_lon),axis=1)


df_lon_1 = pd.read_csv(data_origin+"lon_005.txt")
df_lon_1.columns = ['lon']
df_lat_1 = pd.read_csv(data_origin+"lat_005.txt")
df_lat_1.columns = ['lat']

print(df_lon_1.head())
print(df_lat_1.head())
df_1 = pd.concat((df_lat_1,df_lon_1),axis=1)



#print(df.lon)
gdf  = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.lon,df.lat))
gdf1 = geopandas.GeoDataFrame(df_1, geometry=geopandas.points_from_xy(df_1.lon,df_1.lat))


print(gdf)
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world[world.continent == 'Asia'].plot(color='white',edgecolor='black')
gdf.plot(ax=ax, color='red',marker='.',markersize=0.1)
gdf1.plot(ax=ax, color='green',marker='.',markersize=0.1)

plt.show()
