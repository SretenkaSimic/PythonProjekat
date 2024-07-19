import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


df = pd.read_csv('D:\\Gis Peulić\\Karte\\Karte ex.csv')

print(df.head())

gdf = gpd.read_file('D:\\Gis Peulić\\Karte\\Rasinski okrug.shp')

print(gdf.head())

merged_data = gdf.merge(df, on='ID1')
print(merged_data.head())

import matplotlib.colors as mcolors

bins = [0, 200, 400, 500, 700, 1600]
labels = ['0-200', '200-400', '400-500', '500-700', '700-1600']

cmap = plt.get_cmap('Blues', len(bins) - 1)
norm = mcolors.BoundaryNorm(boundaries=bins, ncolors=len(bins) - 1)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged_data.plot(column='srbi__y', cmap=cmap, norm=norm, legend=False, ax=ax)

for x, y, label in zip(merged_data.geometry.centroid.x, merged_data.geometry.centroid.y, merged_data['Opstina_x']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center')

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, boundaries=bins, ticks=[(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)])
cbar.ax.set_yticklabels(labels)

ax.set_title('Stradali Srbi u Rasinskom okrugu 1941-1945', fontsize=15)

bins1 = [0, 400, 800, 1500, 3000, 8000]
labels1 = ['0-400', '400-800', '800-1500', '1500-3000', '3000-8000']

cmap = plt.get_cmap('OrRd', len(bins1) - 1)
norm = mcolors.BoundaryNorm(boundaries=bins1, ncolors=len(bins1) - 1)
fig, ax1 = plt.subplots(1, 1, figsize=(10, 10))
merged_data.plot(column='ukupno_y', cmap=cmap, norm=norm, legend=False, ax=ax1)

for x, y, label in zip(merged_data.geometry.centroid.x, merged_data.geometry.centroid.y, merged_data['Opstina_x']):
    ax1.text(x, y, label, fontsize=8, ha='center', va='center')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax1, boundaries=bins, ticks=[(bins1[i] + bins1[i+1]) / 2 for i in range(len(bins1)-1)])
cbar.ax.set_yticklabels(labels1)

ax1.set_title('Ukupno stradali u Rasinskom okrugu 1941-1945', fontsize=15)

plt.show()
