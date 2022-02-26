# File for testing the flood submodule in floodsystem

def test_stations_level_over_threshold():
    relative_water_level1 = 0.8
    relative_water_level2 = 0.6
    tolerance = 0.7

    # Check whether logic correct for comparing relative water levels of each station against the defined tolerance value
    assert relative_water_level1 > tolerance
    assert relative_water_level2 < tolerance

def test_stations_highest_rel_level():
    station_number = 3
    example_list = [1, 43, 4, 6, 8, 5]

    assert example_list[:station_number] == [1, 43, 4]