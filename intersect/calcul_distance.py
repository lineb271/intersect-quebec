from math import radians, sin, cos, acos


def calcul_distance(pos_lat, pos_lon, int_lat, int_lon):
    pos_lat = radians(pos_lat)
    pos_lon = radians(pos_lon)
    int_lat = radians(int_lat)
    int_lon = radians(int_lon)

    return 6371.01 * acos(sin(pos_lat)*sin(int_lat) + cos(pos_lat)*cos(int_lat)*cos(pos_lon-int_lon))
