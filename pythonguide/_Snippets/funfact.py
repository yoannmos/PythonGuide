import math


def earth_thickness(distance):
    """ Return the thickness of earth for a given distance"""
    EARTH_RADIUS = 6371  # km
    theta = distance / EARTH_RADIUS
    h = EARTH_RADIUS * (1 - math.cos(theta / 2))
    msg = print("For", distance, "km, the earth thickness is ", round(h, 3), "km .")
    return h, msg


et = earth_thickness(40)
# print(et)
