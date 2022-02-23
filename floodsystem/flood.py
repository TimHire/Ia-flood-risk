# Contains function for assessing the flood risk at different stations

from json import tool


def stations_level_over_threshold(stations, tol):
    # Function for writing the code for Task 2B part 2
    output_list=[]
    # create a empty list
    for station in stations:
        if relative_water_level > tol:
            #make comprison with tol
            output_list += station
            #add the above one to the list
    above_list = sort(output_list)
    return above_list
     # Need to get rid of this when writing the function


def stations_highest_rel_level(stations, N):
    # Function for writing the code for Task 2C
    sort(stations)
    #sort the stations by the value of the N?
    return stations
    
     # Need to get rid of then when writing the function