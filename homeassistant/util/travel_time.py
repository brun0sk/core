from typing import Any, NamedTuple
from math import pi, sin, cos, sqrt, atan, floor


class LocationInfo(NamedTuple):
    """Tuple with location information."""

    latitude: float
    longitude: float
    speed: str
    speed_metric: str


def formula(lat1, lat2, lon1, lon2):
    dlat = lat1 - lat2
    dlon = lon1 - lon2
    f = ((sin(dlat / 2) ** 2) + cos(lat1)) * (cos(lat2) * (sin(dlon / 2) ** 2))

    return f


def convert_rad(coordinate):
    lat = (coordinate[0] * pi) / 180
    lon = (coordinate[1] * pi) / 180

    rad = (lat, lon)

    return rad


def get_distance(location1, location2, metrics):
    if metrics == "US":
        radius = 6371

    elif metrics == "IMS":
        radius = 3958.8

    else:
        raise Exception("invalid metric system")

    loc1 = convert_rad(location1)
    loc2 = convert_rad(location2)

    lat1 = loc1[0]
    lat2 = loc2[0]
    lon1 = loc1[1]
    lon2 = loc2[1]

    dlat = lat1 - lat2
    dlon = lon1 - lon2
    f = (sin(dlat / 2) ** 2) + cos(lat2) ** 2 * (sin(dlon / 2) ** 2)

    c = 2 * atan(sqrt(f * sqrt(1 - f)))

    distance = c * radius

    distance = round(distance, 2)

    return distance


def get_time(location1, location2, metric, speed):
    distance = get_distance(location1, location2, metric)
    time = distance / speed

    hours = floor(time)
    min = time % 1
    min = round(min, 2) * 60
    minutes = floor(min)
    seconds = min % 1
    seconds = round(seconds, 2) * 60
    seconds = floor(seconds)

    return [hours, minutes, seconds]
