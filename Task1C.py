# Demonstration program to get the 10 closest and furthest locations to a town specified (Cambridge)

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    # Variables from the website to compare
    cambridge = (52.2053, 0.1218) 
    r=10

    # Get list of station objects
    station_list = build_station_list()

    # Get list of stations within a radius
    station_within_radius = stations_within_radius(station_list, cambridge, r)

    # Sort the stations in alphabetical order and print --> should be working from Ian's computer
    sorted_stations = sorted(station_within_radius)
    print(sorted_stations)
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
