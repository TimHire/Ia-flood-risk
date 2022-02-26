# Contains function for assessing the flood risk at different stations

from json import tool
from .utils import sorted_by_key
from .station import inconsistent_typical_range_stations


def stations_level_over_threshold(stations, tol):
    # Function for writing the code for Task 2B part 2
    # Get a list of inconsistent stations
    inconsistent = inconsistent_typical_range_stations(stations)

    # Create a empty list
    output_list = []
    # Iterate through all the stations in the station list
    for station in stations:
        # Compare current relative water level with tol
        if station.relative_water_level() is None:
            pass
        elif (station.relative_water_level() > tol) and (station.name not in inconsistent):
            relative_level = station.relative_water_level()
            # Add the above station to the output list
            output_list.append((station, relative_level))
    
    # Sort the output list by the relative water height
    above_list = sorted_by_key(output_list, 1, True)
    return above_list


def stations_highest_rel_level(stations, N):
    # Function for writing the code for Task 2C - returns the N highest relative height stations
    
    # Get a list of all the relative height of the stations
    relative_level_list = stations_level_over_threshold(stations, 0)

    # Return the stations with the 10 highest relative ranges
    return relative_level_list[:N]