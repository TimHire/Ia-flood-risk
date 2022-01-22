# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    # Create empty list to append tuples of (station, distance) to
    output_list = []

    # Iterate through all stations in the list to work out the distance between p and the station
    for station in stations:
        # Get the coordinates of the station
        distance = haversine(station.coord, p)

        # Append the tuple to the output list
        output_list.append((station, distance))

    # Sort the list so by shortest distance
    sorted_by_key(output_list, 1)
    return output_list
