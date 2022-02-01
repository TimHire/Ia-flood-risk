""" This module contains the code for plotting the water level data against time for a station. 
    Will include lines for the typical low and high levels """

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from .analysis import polyfit


def plot_water_levels(station, dates, levels):
    # Find the number of data points being plotted
    data_points = len(dates)

    # Create lists with the typical range values with number of data points corresponding with the number of dates
    min = [station.typical_range[0]] * data_points
    max = [station.typical_range[1]] * data_points

    # Set the figure size
    plt.subplots(figsize=(5, 5))

    # Plot the overall data of levels against time
    plt.plot(dates, levels)

    # Plot the orange lines for max and min of the typical ranges of data
    plt.plot(dates, min, color="orange")
    plt.plot(dates, max, color="orange")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: {}".format(station.name))

    # Display the plot, ensuring no labels are cut off
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    p_coeff, offset = polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)

    # Find the number of data points being plotted
    data_points = len(dates)

    # Create lists with the typical range values with number of data points corresponding with the number of dates
    min = [station.typical_range[0]] * data_points
    max = [station.typical_range[1]] * data_points

    # Set the figure size
    plt.subplots(figsize=(5, 5))

    # Plot the overall data of levels against time
    plt.plot(dates, levels)

    # Plot the orange lines for max and min of the typical ranges of data
    plt.plot(dates, min, color="orange")
    plt.plot(dates, max, color="orange")


    plt.plot(dates, poly(levels), color="green")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: {}".format(station.name))

    # Display the plot, ensuring no labels are cut off
    plt.tight_layout()
    plt.show()