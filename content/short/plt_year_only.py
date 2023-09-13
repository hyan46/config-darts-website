#%%
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
# from uszipcode.search import SearchEngine




#%%
def create_map(min, max, df_HIV_maps, df_zipcodes):
  year_min = int(min)
  year_max = int(max)
  # df_HIV_maps = pd.read_pickle("./HIVE_map.pkl")
  # df_zipcodes = pd.read_pickle("./zipcode_map.pkl")
  fig, ax = plt.subplots(1, figsize=(50, 50))
  df_HIV_maps_year = df_HIV_maps[(df_HIV_maps['year'] >= year_min) & (df_HIV_maps['year'] <= year_max)]
  df_HIV_count_zipcode = df_HIV_maps_year.groupby(['zipcode'], group_keys=False, as_index=False).sum()[
      ['zipcode', 'count']]
  df_HIV_maps_year_merge = df_zipcodes.merge(df_HIV_count_zipcode, on='zipcode', how='outer')
  df_HIV_maps_year_merge = df_HIV_maps_year_merge[
      ~df_HIV_maps_year_merge.state.isin(['AK', 'HI', 'AA', 'AE', 'AP', 'PR', 'RI', 'VI'])]
  df_HIV_maps_year_merge = df_HIV_maps_year_merge[df_HIV_maps_year_merge.state.isin(['WA'])]

  df_HIV_maps_year_merge['count'] = df_HIV_maps_year_merge['count'].fillna(0)
  ax.axis('off')
  df_HIV_maps_year_merge.plot(column='count', edgecolor='0.9', ax=ax, vmin=-5, vmax=5, cmap='seismic')

  plt.title(str(year_min), fontsize=40)
  plt.savefig("{}.png".format(year_min))

  #%%
  m = df_HIV_maps_year_merge.explore(column='count', vmin=-5, vmax=5, cmap='seismic')
  #m = df_HIV_maps_year_merge.explore(column='count', edgecolor='0.9', ax=ax, vmin=-5, vmax=5, cmap='seismic')
  # m.save('yearggg{}.html'.format(year_min))
  return m
