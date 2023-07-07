from .api import base_api

def get_state(country, zip):
    relative_url = f"{country}/{zip}"
    response = base_api.get(relative_url)
    data = response.json()
    
    return data['places'][0]['state']
