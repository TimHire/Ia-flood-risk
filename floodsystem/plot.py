""" This module contains the code for plotting the water level data against time for a station. 
    Will include lines for the typical low and high levels """

import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    # Where dates is the number of days prior you want to plot the data of

    #Plot
    plt.subplots(figsize=(5, 5))
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station {}".format(station.name))

    plt.tight_layout()

    plt.show()
