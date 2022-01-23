from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

# Get list of station objects
station_list = build_station_list()

stations_on_river = rivers_by_station_number(station_list, 9)

print(stations_on_river)