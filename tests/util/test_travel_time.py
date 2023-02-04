import math

import pytest

from homeassistant.util.travel_time import convert_rad, get_distance, get_time


def test_convert_rad():
    location = (-15.7801, -47.9292)
    expected = (-0.2754147012939572, -0.8365223478468663)
    assert convert_rad(location) == expected


def test_get_distance():
    location1 = (-15.7801, -47.9292)
    location2 = (-23.5489, -46.6388)
    metric_system = "US"
    metric_imperial = "IMS"

    assert get_distance(location1, location2, metric_system) == 870.77
    assert get_distance(location1, location2, metric_imperial) == 541.08
    with pytest.raises(Exception) as exc_info:
        get_distance(location1, location2, "error")

    assert str(exc_info.value) == "invalid metric system"


def test_get_time():
    location1 = (-15.7801, -47.9292)
    location2 = (-23.5489, -46.6388)
    metric_system = "US"
    metric_imperial = "IMS"
    speed = 100
    sp = 62.13

    assert get_time(location1, location2, metric_system, speed) == [8, 42, 36]
    assert get_time(location1, location2, metric_imperial, sp) == [8, 42, 36]
