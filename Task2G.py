# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT



# Code written before functions for 2B and 2C were written

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit

def run():
    # Build list of stations
    stations = build_station_list()

    # Define the relative risk for low, medium, moderate, high risk levels
    # If the current water level is in the top 20% of recorded readings, the nearby town has a high flood risk
    risk_boundaries = [0.2, 0.5, 0.8, 1]

    # Get a list of tuples of all the stations in the high risk boundary
    stations_relative_levels_high = stations_level_over_threshold(stations, 0.75)


    # Create an empty set to append the risky towns to --> stops being duplicates if multiple stations for one town
    risky_towns = {}
    for station, relative in stations_relative_levels_high:
        risky_towns.append(station.town)

    # Iterate through the output set, and print the names of the risky towns:
    print("Towns over 0.8 relative levels with high flood risk:")
    for town in sorted(risky_towns):
        print(town)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
