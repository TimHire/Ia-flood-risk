# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from sympy import false


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        # Checks if there are any values assigned to the self.typical_range attribute
        if self.typical_range is None:
            return False

        # Then checks if min greater than max
        elif self.typical_range[0] > self.typical_range[1]:
            return False

        # Returns true for any other case as ranges must be consistent
        else:
            return True

def inconsistent_typical_range_stations(stations):
    # Creates list to append inconsistent stations to 
    output_list = []

    # Iterations through all the stations in the station list
    for station in stations:
        # If inconsistent range, append to the output_list
        if station.typical_range_consistent() == False:
            output_list.append(station.name)
    
    # Return the output_list sorted by alphabetical order of name
    return sorted(output_list)