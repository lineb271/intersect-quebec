# from calcul_distance import calcul_distance
#
# dist = calcul_distance(pos_lat, pos_lon, int_lat, int_lon)


def dist_threshold(dist):
    threshold = 95
    return dist < threshold
