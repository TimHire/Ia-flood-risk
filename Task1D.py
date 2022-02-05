# Demonstration program to get the 10 closest and furthest locations to a town specified (Cambridge)

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    # Get list of station objects
    station_list = build_station_list()

    # Get the list of stations in alphabetical order
    rivers_with_stations = sorted(rivers_with_station(station_list))

    # Get number of stations with more than 1 monitoring station
    number_stations = len(rivers_with_stations)

    # Print the output in the right format
    print("{} stations. First 10 - {}".format(number_stations, rivers_with_stations[:10]))

    # Get the dictionary with the stations on the rivers
    river_dict = stations_by_river(station_list)

    # Get the list of station objects for each river
    r_aire = river_dict["River Aire"]
    r_cam = river_dict["River Cam"]
    r_thames = river_dict["River Thames"]

    # Iterate through one river at a time
    for stations in [r_aire, r_cam, r_thames]:

        # Create an empty list for appending the station names to 
        output_list = []

        # Iterate through all the stations in the list of station objects
        for station in stations:
            # Append the name of the station to output_list
            output_list.append(station.name)

        # Print the sorted output_list in alphabetical order
        print(sorted(output_list))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
