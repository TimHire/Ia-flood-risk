# Demonstration program to get the 10 closest and furthest locations to a town specified (Cambridge)

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    cambridge = (52.2053, 0.1218) 
    r=10

    # Get list of station objects
    station_list = build_station_list()

   


    # Pack first 10 and last 10 into tuple for more efficient coding
    first_last = (ordered_distance_list[:10], ordered_distance_list[-10:])
    for end in first_last:
        output_list = []

        # For first and last 10 in turn, append name, town and distance as a tuple to the output_list
        for i in range(10):
            output_list.append((end[i][0].name, end[i][0].town, end[i][1]))

        # Print the first or last list in turn
        print(output_list)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
