# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels

def run():
    print("Has started the run function")
    
    # Build list of stations
    stations = build_station_list()

    days_to_plot = 10
    number_highest_flow_to_plot = 5

    update_water_levels(stations)
    station_heights = []
    for station in stations:
        station_heights.append([station, station.latest_level])

    sorted_heights = sorted_by_key(station_heights, 1)

    for station in sorted_heights[:number_highest_flow_to_plot]:
        dates, levels = fetch_measure_levels(station.measure_id, days_to_plot)
        plot_water_levels(station[0], dates, levels)

    print("Should have plotted the 5 graphs")


    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
