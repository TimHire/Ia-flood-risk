# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from numpy import number
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    # Function to return a list of all the distances from every station to a specified point p

    # Create empty list to append tuples of (station, distance) to
    output_list = []

    # Iterate through all stations in the list to work out the distance between p and the station
    for station in stations:
        # Get the coordinates of the station
        distance = haversine(station.coord, p)

        # Append the tuple to the output list
        output_list.append((station, distance))

    # Sort the list so by shortest distance
    sorted_output = sorted_by_key(output_list, 1)
    return sorted_output


def rivers_by_station_number(stations, N):
    # Function to return the number of stations on each river

    # Create empty dictionary to keep track of the number of stations on each river
    number_of_stations_dict = {}

    # Iterating through all stations in the database
    for station in stations:
        # If river already has an entry in the dictionary, adds 1 to the count
        if station.river in number_of_stations_dict:
            number_of_stations_dict[station.river] += 1
        
        # If no entry for the river in the dictionary, creates a new item with a count of 1
        else:
            number_of_stations_dict[station.river] = 1
    
    # Creates empty list for appending tuples to
    output_list = []

    # Iterate through the dictionary to append the tuples in the right format to the output_list
    for river, number in number_of_stations_dict.items():
        output_list.append((river, number))

    # Sort the list by the number of stations with the highes first
    sorted_output = sorted_by_key(output_list, 1, reverse=True)

    # Check consecutively if the next largest river has the same number of stations. If so, increase the number of stations printed
    while sorted_output[N][1] == sorted_output[N - 1][1]:
        N += 1 

    # Return the N rivers with the most stations as a list of tuples
    return sorted_output[:N]