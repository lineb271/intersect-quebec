from calcul_distance import calcul_distance
from dist_threshold import dist_threshold
from sql_requests import sql_requests


def main_dist():
    intervention_longitudes, intervention_latitudes = sql_requests()

    pos_lat = '46'
    pos_lon = '-71'

    lat_lon_inside_threshold = []

    for lat, lon in zip(intervention_latitudes, intervention_longitudes):
        dist = calcul_distance(float(pos_lat), float(pos_lon), float(lat), float(lon))

        if dist_threshold(dist):
            lat_lon_inside_threshold.append([lat, lon])

    print("Intersections avec intervention:")
    # if len(lat_lon_inside_threshold) > 0 :
