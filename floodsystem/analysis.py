"""This module contains a collection of functions related to
fitting trend lines onto water height plots.

"""

import numpy as np
import matplotlib 


def polyfit(dates, levels, p):
    # dates and levels are lists of the input data that was plotted on a graph
    # p is the order of the polynomial to best fit to the data

    dates_floats = matplotlib.dates.date2num(dates)
    dates_normal_range = [dates_floats[0] - x for x in dates_floats]
    #print(dates_normal_range)

    p_coeff = np.polyfit(dates_normal_range, levels, p)

    return (p_coeff, dates_floats[0])

