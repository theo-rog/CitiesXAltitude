# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% Cell 1, imports
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
from pathlib import Path

# Data import from root 
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "cities_check_ID.csv"
cities = pd.read_csv(file_path)

#%% Cell 2, data manipulation

# Log transform the haversine distance and population ratio (with small constant to avoid log(0))
cities["log haversine"] = np.log10(cities['haversine_km'] + 0.000001)
cities["log ALPR"] = np.log10(cities['ALPR']+ 0.000001)

# Counting how many times each unique ID appears in the dataset
max_id_count = cities[["simple_id_count", "cities_id_count"]].max(axis=1)

#%% Cell 3, plotting

# Colour map
norm = mcolors.Normalize(vmin=2, vmax=max_id_count.max())
cmap = plt.colormaps['YlOrRd']

def count_2_colour(count):
    if count == 1:
        return("green")
    else:
        return(cmap(norm(count)))



def plot_scatter(log_dist = True,log_pop = True,x_boundary = 3,y_boundary = 30):


    x = cities['log ALPR'] if log_pop else cities['ALPR']
    y = cities['log haversine'] if log_dist else cities['haversine_km']

    plt.scatter(
       x,y,
        s = 0.3,
        alpha = 1,
        c = max_id_count.apply(count_2_colour),

        )


    x_line = np.log10(x_boundary) if log_pop else x_boundary
    y_line = np.log10(y_boundary) if log_dist else y_boundary
    plt.axvline(x_line, color='purple', linestyle='--')
    plt.axhline(y_line, color='blue', linestyle='--')

    plt.xlabel("ALPR (log)" if log_pop else "ALPR")
    plt.ylabel("Haversine Distance (log)" if log_dist else "Haversine Distance")
    plt.title("Matching Cities from Simple and cities1000 datasets")
    plt.show()

#%% Cell 4, run the function
plot_scatter(log_dist=True,log_pop=True)
# %%
