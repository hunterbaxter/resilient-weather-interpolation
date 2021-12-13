from kafka import KafkaConsumer
from typing import List
from pandas import Timestamp
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
from scipy.interpolate import griddata

# LON THEN LAT

dummy_data = {
    'center1': [
        {
            "rh": 68,
            "pod": "n",
            "lon": -86.79,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.15,
            "weather": {
                "icon": "c04n",
                "code": 804,
                "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 69,
            "pod": "n",
            "lon": -86.79,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.15,
            "weather": {
                "icon": "c04n",
                "code": 804,
                "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },                {
            "rh": 70,
            "pod": "n",
            "lon": -86.79,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.15,
            "weather": {
                "icon": "c04n",
                "code": 804,
                "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
    ],
    'center2': [
        {
            "rh": 58,
            "pod": "n",
            "lon": -86.77,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 59,
            "pod": "n",
            "lon": -86.77,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 60,
            "pod": "n",
            "lon": -86.77,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 61,
            "pod": "n",
            "lon": -86.77,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },

    ],
    'center3': [

        {
            "rh": 48,
            "pod": "n",
            "lon": -86.78,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.13,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 49,
            "pod": "n",
            "lon": -86.78,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.13,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
    ],
    'center4': [
        {
            "rh": 55,
            "pod": "n",
            "lon": -86.8,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
        {
            "rh": 56,
            "pod": "n",
            "lon": -86.8,
            "pres": 994.3,
            "timezone": "America/Chicago",
            "ob_time": "2021-12-12 00:50",
            "aqi": 18,
            "lat": 36.14,
            "weather": {
                        "icon": "c04n",
                        "code": 804,
                        "description": "Overcast clouds"
            },
            "datetime": "2021-12-12:01",
            "temp": 5.9,
            "station": "0505W",
            "elev_angle": -28.46,
            "app_temp": 5.9
        },
    ]
}


class KafkaWeather():

    def __init__(self, station_list, broker_ip):
        self.station_dict = dict()
        self.number = 0

        # Setting up dictionary to hold most recent weather info
        self.build_station_dict_from_list(station_list)

        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.update_map, trigger="interval", seconds=10)
        scheduler.start()
        self.update_map()

    def build_station_dict_from_list(self, station_list):
        for station in station_list:
            self.station_dict[station] = {
                'latest_data': None, 'topic': dummy_data[station]}

    def build_station_dict_from_kafka(self, station_list, ip):
        for station in station_list:
            listener = KafkaConsumer(bootstrap_servers=ip)
            listener.subscribe(topics=[str(station)])
            self.station_dict[station] = {
                'latest_data': None, 'topic': listener}

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

    def get_latest_value_from_kafka(self, kafka_consumer):
        try:
            val = next(kafka_consumer)
            return val
        except:
            return None

    def get_latest_value_from_list(self, lst: List):
        return (lst.pop(0) if len(lst) > 0 else None)

    def simplify_data(self, data, field='rh'):
        return {
            'lat': data['lat'],
            'lon': data['lon'],
            'value': data[field]
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
