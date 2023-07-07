from .api import base_api
import os
apiKey = os.environ.get('OPEN_WEATHER_MAP_API_KEY')


def get_lat_lon(city, stateCode, countryCode):
    if not city or not countryCode:
        raise Exception('City and Country code must be specified')

    relativeUrl = 'geo/1.0/direct'
    params = {
        'q': f'{city},{stateCode},{countryCode}',
        'limit': 1,
        'appid': apiKey
    }

    try:
        response = base_api.get_with_params(relativeUrl, params)
        data = response.json()

        if len(data) == 0:
            raise Exception(
                f'Failed to retrieve latitude and longitude for {city}')

        return {
            'lat': data[0]['lat'],
            'lon': data[0]['lon']
        }
    except Exception as error:
        raise Exception(str(error))


def get_weather_data(lat, lon):
    if not lat or not lon:
        raise Exception('Latitude and longitude must be specified')

    try:
        relativeUrl = 'data/2.5/weather'
        params = {
            'lat': lat,
            'lon': lon,
            'appid': apiKey
        }
        response = base_api.get_with_params(relativeUrl, params)

        return response.json()
    except Exception as error:
        raise Exception(f'Failed to fetch weather data: {str(error)}')
