import json
import requests

class Weather(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


class WeatherService():
    def __init__(self, *args, **kwargs):

        def parseJson(self):
            import pdb
            pdb.set_trace()
            return 1

        self.parseJson = parseJson(self)


base_url = 'https://api.openweathermap.org/data/2.5'
payload = {
    'q': 'Paris',
    'appid': '5ab21a7d11964ffa58b9f5966a91f6c6',
    'units': 'metric',
}
url = base_url + '/weather'

r = requests.get(url, params=payload)
json_data = r.status_data
print(json_data)
# weather_service = WeatherService()
# weather = weather_service.parseJson(json_data)

weather = Weather(json_data)
print(weather)
