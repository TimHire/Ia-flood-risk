from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    # Get list of station objects
    station_list = build_station_list()

    # Get list of inconsistent stations sorted by name
    inconsistent_stations = inconsistent_typical_range_stations(station_list)

    print(inconsistent_stations)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()