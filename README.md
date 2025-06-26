
# Cities x Altitude

## Overview
This project consists of two parts:
1. Joining two datasets of global cities
    - Requires identifying which cities match with each other - City name and country prove insufficient
    - Use of location and population to identify similarity
    - Provides a dataset with accurate list of cities with information on location and population, used for:
2. Using the dataset to analyse cities' population against altitude (to be completed)

## Datasets
- simplemaps dataset (source provided in report): 
    - Reputable dataset with 48,056 cities
    - Name, country, co-ordinates and population
    - Requires inclusion of altitude
- geonames dataset:
    - Dataset with 154,694 cities
    - Name, country, co-ordinates, population and elevation
    - Used to include altitude of cities

(source provided in report)

## Skills demonstrated
- SQL joins, filtering, ID validation
- Population ratio metric (ALPR)
- Haversine distance
- Visualisation of matching quality
- Data cleaning & edge case handling (e.g. Springfield)

## Structure
Part 1/
├── cities database.db           # Final SQLite database
├── city sample check.xlsx       # Manual verification of known cities
├── python/                      # Python scripts for visualisation
│   ├── cities_check_ID.csv      
│   ├── cities_check_vis.py
│   └── geonames_vis.ipynb
├── Reports/
│   ├── CITYxALT_part1_report.ipynb # Report describing process and giving more detailed overview
│   └── plots_part1/             # All figures used in report part 1
└── Part 2/                      # Placeholder for continuation

## Future work
- Part 2 will explore altitude/population relationships using the merged dataset

## Note
This is a project completed independently for personal enjoyment/learning. The primary goal of this project is for me to learn and demonstrate my learning of SQL - accordingly there is room for polish in the report writing, and rigour in methodology.

## Contact
Feel free to get in touch via GitHub or LinkedIn (https://www.linkedin.com/in/theo-rogers-15ab4a225/) if you’d like to know more.