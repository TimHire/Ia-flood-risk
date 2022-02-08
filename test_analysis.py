# File for testing the floodsystem.analysis file

import numpy as np

def test_polyfit():
    dates = list(range(0, 50))
    levels = [x**5 + 4 * x**4 - 2 * x + 156 for x in dates]

    n = 5

    p_coeff = np.polyfit(dates, levels, n)
    
    assert round(p_coeff[0]) == 1
    assert round(p_coeff[1]) == 4
    assert round(p_coeff[2]) == 0
    assert round(p_coeff[3]) == 0
    assert round(p_coeff[4]) == -2
    assert round(p_coeff[5]) == 156