# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## cells, comments, functions
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd


data_link = '/Users/theorogers/Desktop/SkillsyBits/Projects/SQL/cities project/cities_check_IDcounts.csv'
cities = pd.read_csv(data_link)

cities["log haversine"] = np.log(cities['haversine_km'])
cities["log pop_ratio"] = np.log(cities['pop_ratio'])
max_id_count = cities[["simple_id_count", "cities_id_count"]].max(axis=1)

norm = mcolors.Normalize(vmin=2, vmax=max_id_count.max())
cmap = cm.get_cmap('YlOrRd')

def count_2_colour(count):
    if count == 1:
        return("green")
    else:
        return(cmap(norm(count)))

plt.scatter(
    cities['log pop_ratio'],cities["log haversine"],
    s = 0.3,
    alpha = 1,
    c = max_id_count.apply(count_2_colour),

    )
plt.axhline(np.log(3), color='blue', linestyle='--')
plt.axvline(np.log(30), color='purple', linestyle='--')
plt.xlabel("Population Ratio (log0")
plt.ylabel("Haversine Distance (log)")
plt.title("Matching Cities from Simple and cities1000 datasets")