import pytest
from .questions import get_lat_lon, get_weather_data


@pytest.mark.api
def test_getWeatherData_valid_location():
    # Arrange
    city = 'London'
    stateCode = ''
    countryCode = 'GB'

    # Act
    result = get_lat_lon(city=city, stateCode=stateCode,
                         countryCode=countryCode)
    lat = result['lat']
    lon = result['lon']
    weatherData = get_weather_data(lat=lat, lon=lon)

    # Assert
    assert isinstance(weatherData, dict)
    assert weatherData['name'] == city
    assert 'temp' in weatherData['main']
    assert 'description' in weatherData['weather'][0]


@pytest.mark.api
def test_getWeatherData_missing_coordinates():
    # Arrange
    lat = None
    lon = None

    # Act & Assert
    with pytest.raises(Exception) as e:
        get_weather_data(lat=lat, lon=lon)

    error_message = str(e.value)
    assert error_message == 'Latitude and longitude must be specified'
