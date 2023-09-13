#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from uszipcode.search import SearchEngine

X_Diag_Dataset = pd.read_excel('Randomized Sample.xlsx')

date_columns = ['diag_date','case_report_date']
for i_date in date_columns:
    X_Diag_Dataset[i_date] = pd.to_datetime(X_Diag_Dataset[i_date],format="%Y%m%d")

zip_columns = ['diag_zip','diag_provider_zip']
for i_zip in zip_columns:
    X_Diag_Dataset[i_zip] = X_Diag_Dataset[i_zip].astype('Int64').astype(str)
X_Diag_Dataset.rename(columns={'diag_zip':'zipcode'}, inplace=True)
X_Diag_Dataset['count'] = np.ones(100)

X_Diag_Dataset.head(10)

#%%
df_zipcodes = gpd.read_file('shape/cb_2017_us_zcta510_500k.shp')
df_zipcodes.rename(columns={'ZCTA5CE10':'zipcode'}, inplace=True)
search = SearchEngine()
df_zipcodes['state'] = df_zipcodes.apply(lambda row: search.by_zipcode(row.zipcode).state, axis=1)
df_zipcodes['county'] = df_zipcodes.apply(lambda row: search.by_zipcode(row.zipcode).county, axis=1)
df_zipcodes.head(10)

df_HIV_maps = X_Diag_Dataset.merge(df_zipcodes, on='zipcode', how='left')
df_HIV_maps['count'] = np.ones(100)
df_HIV_maps['year'] = df_HIV_maps['diag_date'].dt.year


#%%
year = 2021
fig, ax = plt.subplots(1, figsize=(50, 50))
df_HIV_maps_year = df_HIV_maps[df_HIV_maps['year'] == year]
df_HIV_count_zipcode = df_HIV_maps_year.groupby(['zipcode'], group_keys=False, as_index=False).sum()[
    ['zipcode', 'count']]
df_HIV_maps_year_merge = df_zipcodes.merge(df_HIV_count_zipcode, on='zipcode', how='outer')
df_HIV_maps_year_merge = df_HIV_maps_year_merge[
    ~df_HIV_maps_year_merge.state.isin(['AK', 'HI', 'AA', 'AE', 'AP', 'PR', 'RI', 'VI'])]
df_HIV_maps_year_merge = df_HIV_maps_year_merge[df_HIV_maps_year_merge.state.isin(['WA'])]

df_HIV_maps_year_merge['count'] = df_HIV_maps_year_merge['count'].fillna(0)
ax.axis('off')
df_HIV_maps_year_merge.plot(column='count', edgecolor='0.9', ax=ax, vmin=-5, vmax=5, cmap='seismic')

plt.title(str(year), fontsize=40)
plt.savefig("{}.png".format(year))

#%%
m = df_HIV_maps_year_merge.explore(column='count', vmin=-5, vmax=5, cmap='seismic')
#m = df_HIV_maps_year_merge.explore(column='count', edgecolor='0.9', ax=ax, vmin=-5, vmax=5, cmap='seismic')
m.save('year{}.html'.format(year))
