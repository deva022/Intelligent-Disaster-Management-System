import requests

class DataPoint:
    def __init__(self, data_type, location, timestamp, value):
        self.data_type = data_type
        self.location = location
        self.timestamp = timestamp
        self.value = value

class DataCollector:
    def __init__(self):
        self.data_points = []

    def collect_data(self):
        response = requests.get('https://api.weatherapi.com/v1/current.json?key={api_key}=Ahmedabad')
        weather_data = response.json()
        print(weather_data)
        data_point = DataPoint('weather', 'London', weather_data['location']['localtime'], weather_data['current']['temp_c'])
        self.data_points.append(data_point)
        
