# File for testing the plot submodule in floodsystem

import numpy as np

def testing_best_fit_plotting():
    """ Function for testing the plotting of the line of best fit """
    dates = list(range(0, 50))
    levels = [x**5 + 4 * x**4 - 2 * x + 156 for x in dates]

    n = 5

    p_coeff = np.polyfit(dates, levels, n)  
    poly = np.poly1d(p_coeff)

    assert poly(156) == -239441.47360061095