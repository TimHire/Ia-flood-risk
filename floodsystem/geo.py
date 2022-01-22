# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    output_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        output_list.append((station, distance))
    sorted_by_key(output_list, 1)
    return output_list
