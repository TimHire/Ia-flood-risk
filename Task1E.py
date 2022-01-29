from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    # Get list of station objects
    station_list = build_station_list()

    # Call function to get 9 rivers ranked by most monitoring stations on them, or more if same number of stations on different rivers
    stations_on_river = rivers_by_station_number(station_list, 9)

    # Print the output to the terminal
    print(stations_on_river)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()