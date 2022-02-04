"""This module contains a collection of functions related to
fitting trend lines onto water height plots.

"""

import numpy as np
import matplotlib 


def polyfit(dates, levels, p):
    # dates and levels are lists of the input data that was plotted on a graph
    # p is the order of the polynomial to best fit to the data

    # Convert the date format to a float of the number of days since the beginning of year 0001 --> NEED TO KEEP TRACK OF A SHIFT TO THE TIME AXIS?
    dates_floats = matplotlib.dates.date2num(dates)

    # Normalise the data so the last day from the start is 0
    dates_normal_range = [x - dates_floats[0] for x in dates_floats]

    # Creates a polynomial object with order p which is best fit of the data
    p_coeff = np.polyfit(dates_normal_range, levels, p)

    # returns tuple of (polynomial object, shift to the time axis)
    return (p_coeff, dates_floats[0])

