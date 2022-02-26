# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels

def run():
   
    # Build list of stations
    stations = build_station_list()

    # Set number of days and stations to plot --> specified in the documentation
    days_to_plot = 2
    number_highest_flow_to_plot = 5
    polynomial_level = 4

    # Update the current water levels in each station object from the internet
    update_water_levels(stations)

    # Create empty list for storing tuples of station object and current height
    station_heights = []

    # Iterate through all stations to append tuple of station object and current height
    for station in stations:

        level = station.latest_level

        # Check if latest_level object is None. If so, change to 0 as helps later sorting algorithms
        if level == None:
            level = 0

        station_heights.append((station, level))

    # Sort the final lists of tuples by the current height of the river
    sorted_heights = sorted_by_key(station_heights, 1, reverse=True)

    # Iterate through the first 5 stations (or number specified)
    for station in sorted_heights[:number_highest_flow_to_plot]:
        try:
            # Get lists of dates and levels 
            dates, levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=days_to_plot))
            print(dates, levels)
            # Call the plotting function to plot each station one at a time
            plot_water_level_with_fit(station[0], dates, levels, polynomial_level)

        except:
            # Data is not linear so an error in the best fit algorithm --> numpy.polyfit throws an error
            print("Data Error: data not linear so cannot find line of best fit")
  


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
