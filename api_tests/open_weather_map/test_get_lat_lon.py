from typing import Dict
import pytest
from .questions import get_lat_lon


@pytest.mark.api
def test_should_return_latitude_and_longitude_for_valid_location():
    # Arrange
    city = 'London'
    state_code = ''
    country_code = 'GB'

    # Act
    result = get_lat_lon(city, state_code, country_code)
    lat = result['lat']
    lon = result['lon']

    # Assert
    assert isinstance(lat, float)
    assert isinstance(lon, float)


@pytest.mark.api
def test_should_throw_error_for_invalid_location():
    # Arrange
    city = 'InvalidCity'
    state_code = ''
    country_code = 'US'

    # Act & Assert
    with pytest.raises(Exception) as e:
        get_lat_lon(city, state_code, country_code)

    error_message = str(e.value)
    assert error_message == f"Failed to retrieve latitude and longitude for InvalidCity"
