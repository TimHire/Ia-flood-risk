# Demonstration program to get the 10 closest and furthest locations to a town specified (Cambridge)

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    cambridge = (52.2053, 0.1218) 
    r=10

    # Get list of station objects
    station_list = build_station_list()

    station_within_radius = stations_within_radius(station_list, cambridge, r)
    print(station_within_radius)

    sorted_output = sort(station_within_radius)
    print(station_within_radius)
    




if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
