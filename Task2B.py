# This is the file for writing the testing programs of Task2B


from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()
    # Update the current water levels in the station objects
    update_water_levels(stations)

    threshold = 0.8
    # Get the list of stations over the relative water level threshold
    over_threshold = stations_level_over_threshold(stations, threshold)

    # Iterate through each station in the output list and print in the correct format
    for entry in over_threshold:
        print(f"{entry[0].name} {entry[1]}")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
