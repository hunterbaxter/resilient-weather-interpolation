# from kafka import KafkaConsumer
from typing import List
from pandas import Timestamp
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
from scipy.interpolate import griddata

# LON THEN LAT

dummy_data = {
    'center1': [
        {'measurement': 'weather',
         'tags': {'lat': 36.15, 'lon': -86.79},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 36.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.15, 'lon': -86.79},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 37.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.13, 'lon': -86.79},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 38.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}}
    ],
    'center2': [
        {'measurement': 'weather',
         'tags': {'lat': 36.14, 'lon': -86.77},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 45.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.14, 'lon': -86.77},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 44.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.14, 'lon': -86.77},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 43.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.14, 'lon': -86.77},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 42.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}}
    ],
    'center3': [
        {'measurement': 'weather',
         'tags': {'lat': 36.13, 'lon': -86.78},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 1.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
        {'measurement': 'weather',
         'tags': {'lat': 36.13, 'lon': -86.78},
         'time': Timestamp('2021-11-28 03:30:00+0000', tz='UTC'),
         'fields': {'wind_cdir': 'SSW', 'rh': 2.0, 'pod': 'n', 'pres': 994.3, 'timezone': 'America/Chicago', 'country_code': 'US', 'clouds': 75.0, 'vis': 5.0, 'wind_spd': 2.06, 'wind_cdir_full': 'south-southwest', 'app_temp': 8.0, 'state_code': 'TN', 'h_angle': -90.0, 'dewpt': -6.3, 'weather_icon': 'c01n', 'weather_code': 800, 'weather_description': 'Clear sky', 'uv': 0.0, 'aqi': 23.0, 'station': 'KBNA', 'wind_dir': 200.0, 'elev_angle': -53.32, 'precip': 0.0, 'ghi': 0.0, 'dni': 0.0, 'dhi': 0.0, 'solar_rad': 0.0, 'city_name': 'Berry Hill', 'sunrise': '12:36', 'sunset': '22:33', 'temp': 8.0, 'slp': 1016.3}},
    ]
}


class KafkaWeather():

    def __init__(self, weather_station_lst, broker_ip):
        self.station_dict = dict()
        self.number = 0

        # Setting up dictionary to hold most recent weather info
        for station in weather_station_lst:
            self.station_dict[station] = {
                'latest_data': None, 'topic': dummy_data[station]}

        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.update_map, trigger="interval", seconds=10)
        scheduler.start()
        self.update_map()

    def get_formatted_data_stream(self):
        data_dictionary = {"type": "FeatureCollection", "features": []}
        # TODO - Add interpolation
        for row in self.get_interpolated_list():
            data_dictionary["features"].append(
                self.format_data(row))
        return data_dictionary

    def get_GeoJSON_data(self):
        formatted_data = self.get_formatted_data_stream()
        return formatted_data

    def update_map(self):
        for station, properties in self.station_dict.items():
            latest_value = self.updated_value(properties)
            if latest_value != None:
                simplified_value = self.simplify_data(latest_value)
                self.station_dict[station]['latest_data'] = simplified_value
        self.number += 1

    def updated_value(self, station_properties):
        return self.get_latest_value_from_list(station_properties['topic'])

    def get_latest_value_from_list(self, lst: List):
        return (lst.pop(0) if len(lst) > 0 else None)

    def simplify_data(self, data, field='rh'):
        return {
            'lat': data['tags']['lat'],
            'lon': data['tags']['lon'],
            'value': data['fields'][field]
        }

    def format_data(self, data):
        return {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [self.create_square(data['lon'], data['lat'])]},
            'properties': {'field': data['value']}
        }

    def create_square(self, lat, lon):
        return [
            [lat + 0.01, lon + 0.01],
            [lat + 0.01, lon - 0.01],
            [lat - 0.01, lon - 0.01],
            [lat - 0.01, lon + 0.01],
            [lat + 0.01, lon + 0.01]
        ]

    def get_interpolated_list(self):

        interpolated_lst = []

        weather_mat = np.array([[station['latest_data']['lon'], station['latest_data']['lat'],
                                 station['latest_data']['value']] for station in self.station_dict.values()])

        point_mat = weather_mat[:, 0:2]
        value_mat = weather_mat[:, 2]

        lon_meshed, lat_meshed = np.meshgrid(
            weather_mat[:, 0], weather_mat[:, 1])

        interpolated_values = griddata(
            point_mat, value_mat, (lon_meshed, lat_meshed), method='nearest')

        interpolated_mat = np.column_stack(
            (lon_meshed.reshape(-1, 1), lat_meshed.reshape(-1, 1), interpolated_values.reshape(-1, 1)))

        for row in interpolated_mat:
            interpolated_lst.append({
                'lon': row[0],
                'lat': row[1],
                'value': row[2]
            })

        return interpolated_lst

        # print('Weather Mat')
        # print(weather_mat)

        # print('lon')
        # print(lon_meshed)
        # print('lat')
        # print(lat_meshed)

        # print('Interpolated Values')
        # print(interpolated_values)

        # print('Interpolated')
        # print(interpolated_mat)

        # print('Return list')
        # print(interpolated_lst)
