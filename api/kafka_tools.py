# from kafka import KafkaConsumer
from pandas import Timestamp
from apscheduler.schedulers.background import BackgroundScheduler

# LON THEN LAT


dummy_data1 = [
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}}
]
dummy_data2 = [
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}}
]
dummy_data3 = [
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    {'measurement': 'weather',
     'tags': {'lat': 36.13, 'lon': -86.67},
     'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
     'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
]


class KafkaWeather():

    def __init__(self, weather_station_lst, broker_ip):
        self.station_dict = dict()
        self.number = 0

        # Setting up dictionary to hold most recent weather info
        for station in weather_station_lst:
            self.station_dict[station] = {
                'latest_value': None, 'topic': 'KafkaConsumer'}
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.update_map, trigger="interval", seconds=5)
        scheduler.start()

    # def get_stream_from_kafka():
    #     consumer = KafkaConsumer()

    def format_data_stream(self, stream):
        data_dictionary = {"type": "FeatureCollection", "features": []}
        for row in stream:
            data_dictionary["features"].append(self.format_data(row))
        return data_dictionary

    def format_data(self, data):
        return {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [self.create_square(data['tags']['lat'], data['tags']['lon'])]}
        }

    def create_square(self, lat, lon):
        return [
            [lat + 0.01, lon + 0.01],
            [lat + 0.01, lon - 0.01],
            [lat - 0.01, lon - 0.01],
            [lat - 0.01, lon + 0.01],
            [lat + 0.01, lon + 0.01]
        ]

    def get_GeoJSON_data(self):
        formatted_data = self.format_data_stream(dummy_data1)
        return "<h1>Resilient Weather Kriging " + str(self.number) + " </h1>"

    def update_map(self):
        self.number += 1
