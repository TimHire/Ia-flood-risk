# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT



# Code written before functions for 2B and 2C were written
import datetime
import numpy as np
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def run():
    # Build list of stations
    stations = build_station_list()

    # DEFINITION OF SOME OF THE CONSTANTS FOR NUMBERICALLY DEFINING THE RISK LEVELS OF EACH TOWN
    # Define the relative risk for severe, high, moderate, low risk levels
    relative_level_risk_boundaries = [0.2, 0.5, 0.8, 1]
    gradient_risk_boundaries = [-2, 0, 2]
    risk_names = ["low", "moderate", "high", "severe"]
    importance_of_gradient = 0.05                       # Number to bias the risk factor depending on final gradient of the graph

    # Get a list of tuples of all the stations and their associated relative risk levels
    stations_relative_levels_high = stations_level_over_threshold(stations, 0)

    # DEFINE CONSTANTS FOR WORKING OUT THE RISK LEVELS OF ALL THE TOWNS ON THE MAP    
    towns_risks = {}        # Create an empty dictionary to append the town:risk to
    n = 6                   # define the number of terms in the polynomial to set the accuracy of the measurements
    days_to_plot = 14       # number of past days to get the data for to polynomial fit

    # Iterate through all the stations individually and assess their risk levels
    for station, relative in stations_relative_levels_high:

        # Parse in the data to the polyfit function to get a polynomial which can be diffrentiated to get the change in the flood risk
        # Get the data for the last 10 days
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=days_to_plot))
        
        # Get the polynomial coefficients for the line of best fit
        p_coefficients, offset = polyfit(dates, levels, n)              
        # Convert the polynomial coefficients into a function object
        function = np.poly1d(p_coefficients)                            
        # Get the diffrentiated polynomial object
        diffrentiated_coefficients = np.polyder(function)               

        # Convert the dates to numbers so can be inputted into the diffrentiated function    
        dates_floats = matplotlib.dates.date2num(dates)
        # Turn the dates into a float of the number of days to the start
        final_gradient = diffrentiated_coefficients(dates_floats[-1] - dates_floats[0])     

        # Compare the data to the risk boundaries defined above
        # Change the risk rating depending on the current trend of the water level
        #If the current trend of the data is reducing
        if final_gradient < gradient_risk_boundaries[0]:
            risk_index = relative - importance_of_gradient
        #If the current trend of the data is staying the same
        if (final_gradient > gradient_risk_boundaries[1]) and (final_gradient < gradient_risk_boundaries[2]):
            risk_index = relative
        #If the current trend of the data is increasing
        if final_gradient > gradient_risk_boundaries[2]:
            risk_index = relative + importance_of_gradient

        # Check if the town already has a risk factor associated with it. Only update the risk value if it is greater
        if station.name in list(towns_risks.keys()):
            if risk_index > towns_risks[station.name]:
                towns_risks[station.name] = risk_index
        else:
            towns_risks[station.name] = risk_index

    severe_risk_towns = []
    # Check through the towns_risk list and convert all the risk values to a work risk level
    for town in list(towns_risks.keys()):
        if towns_risks[town] < relative_level_risk_boundaries[0]:
            towns_risks[town] = risk_names[0]
        elif (towns_risks[town] > relative_level_risk_boundaries[0]) and (towns_risks[town] < relative_level_risk_boundaries[1]):
            towns_risks[town] = risk_names[1]
        elif (towns_risks[town] > relative_level_risk_boundaries[1]) and (towns_risks[town] < relative_level_risk_boundaries[2]):
            towns_risks[town] = risk_names[2]
        elif towns_risks[town] > relative_level_risk_boundaries[2]:
            towns_risks[town] = risk_names[3]
            # If have a severe flood risk, also append the town name to the severe_risk_towns list
            severe_risk_towns.append(town)

    # Iterate through the output set, and print the names of the most risky towns:
    print("Towns over 0.8 relative levels with high flood risk:")
    for town in sorted(severe_risk_towns):
        print(town)

    # print(towns_risks)        # Prints the dictionary with all the towns and their associated risk levels


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
