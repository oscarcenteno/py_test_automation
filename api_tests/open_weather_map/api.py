from api_tests.base_api import BaseApi
import env
base_url = env.get('OPEN_WEATHER_API_BASE_URL')
base_api = BaseApi(base_url)
