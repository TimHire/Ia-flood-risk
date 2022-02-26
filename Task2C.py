from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()
    # Update the current water levels in the station objects
    update_water_levels(stations)

    # Get a list of the 10 highest relative levels 
    highest_relative_height = stations_highest_rel_level(stations, 10)

    # Iterate through each station in the output list and print in the correct format
    for entry in highest_relative_height:
        print(f"{entry[0].name} {entry[1]}")
   
  


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
