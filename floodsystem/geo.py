# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from numpy import number
from numpy import sort
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


def stations_within_radius(stations, centre, r):
    # Create empty list for storing stations within radius
    output_list = []

    # Iterate through stations in the list
    for station in stations:
        # Calculate the distance betweeen the individual station and the point
        distance = haversine(station.coord, centre)

        # Compare if the distance is within the radius. If yet, append to the list
        if distance < r:
            output_list.append(station.name)
            
    # Return the output_list 
    return output_list

def rivers_with_station(stations):
    # Create empty list to append rivers to
    output_list = []

    # Iterate through the list of stations
    for station in stations:
        # Append name of river to the list
        output_list.append(station.river)

    # Convert list to a set to remove duplicates
    return set(output_list)


def stations_by_river(stations):
    # Create empty dictionary
    output_dict = {}

    # Iterate through the stations
    for station in stations:
        # Check whether the river already in the dicionary --> append station object to value
        if station.river in output_dict.keys():
            output_dict[station.river].append(station)

        # River not already in the dictionary
        else:
            output_dict[station.river] = [station]

    # Return the dicionary
    return output_dict


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


def stations_level_over_threshold(stations, tol):
    output_list=[]
    # create a empty list
    for station in stations:
        if relative_water_level > tol:
            #make comprison with tol
            output_list += station
            #add the above one to the list
    above_list = sort(output_list)
    return above_list
    




