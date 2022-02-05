# File for testing the floodsystem.geo file

from haversine import haversine

def test_stations_by_distance():
    """ Test finding the distance between two points """
    point1 = (50.0359, 5.4253)
    point2 = (58.3838, 3.0412)

    distance = haversine(point1, point2)

    assert distance == 940.9489257526606

def test_station_within_radius():
    """ Test checking whether a point is within a radius of another point """
    cambridge = (52.2053, 0.1218)
    r = 500

    point1 = (50.0359, 5.4253)
    distance1 = haversine(cambridge, point1)
    if distance1 < r:
        within_radius = True
    else:
        within_radius = False
    assert within_radius == True

    point2 = (58.3838, 3.0412)
    distance2 = haversine(cambridge, point2)
    if distance2 < r:
        within_radius = True
    else:
        within_radius = False
    assert within_radius == False


def testing_rivers_by_station_number():
    """ Test to check can increase the number of a value of a dictionary """
    test_dict = {}
    test_list = [1, 4, 5, 45, 85, 88, 93, 99, 100]

    for number in test_list:
        if number % 2 == 0:
            if "even" in test_dict.keys():
                test_dict["even"] += 1
            else:
                test_dict["even"] = 1
        else:
            if "odd" in test_dict.keys():
                test_dict["odd"] += 1
            else:
                test_dict["odd"] = 1

    assert list(test_dict.keys()) == ["odd", "even"]
    assert list(test_dict.values()) == [6, 3]
