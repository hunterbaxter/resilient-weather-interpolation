from kafka import KafkaConsumer, TopicPartition
from typing import List
from pandas import Timestamp
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
from scipy.interpolate import griddata
import ast

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

    def __init__(self, station_list, ip):
        self.station_dict = dict()
        self.kafka_ip = ip
        self.max_value = 0
        self.min_value = 0
        dumb_consumer = KafkaConsumer(bootstrap_servers=self.kafka_ip)
        self.station_topic_list = dumb_consumer.topics()

        # Setting up dictionary to hold most recent weather info
        # self.build_station_dict_from_list(station_list)
        self.build_station_dict_from_kafka()

        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.update_map, trigger="interval", seconds=60)
        scheduler.start()
        self.update_map()

    def build_station_dict_from_list(self, station_list):
        for station in station_list:
            self.station_dict[station] = {
                'latest_data': None, 'listener': dummy_data[station]}

    def build_station_dict_from_kafka(self):
        for station in self.station_topic_list:
            new_listener = KafkaConsumer(
                bootstrap_servers=self.kafka_ip)
            tp = TopicPartition(station, 0)
            new_listener.assign([tp])
            self.station_dict[station] = {
                'latest_data': None, 'listener': {'consumer': new_listener, 'topic_partition': tp}}

    def get_formatted_data_stream(self):
        data_dictionary = {"type": "FeatureCollection", "features": []}
        interpolated_list = self.get_interpolated_list()
        if interpolated_list == None:
            return {"Error": "No Points"}

        for row in interpolated_list:
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

    def updated_value(self, station_properties):
        return self.get_latest_value_from_kafka(station_properties['listener'])

    def get_latest_value_from_kafka(self, listener):
        listener['consumer'].poll()
        end_offset = listener['consumer'].end_offsets([listener['topic_partition']])[
            listener['topic_partition']]
        if end_offset > 0:
            listener['consumer'].seek(
                listener['topic_partition'], end_offset - 1)
            return ast.literal_eval(
                next(listener['consumer']).value.decode('utf-8'))
        else:
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
        white = [255, 255, 255]
        red = [255, 0, 0]
        temp_step = 255.0 / float((self.max_value - self.min_value))
        steps = float((data['value'] - self.min_value))
        temp_diff = int(temp_step * steps)
        color = [255, 255 - temp_diff, 255 - temp_diff]
        return {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [self.create_square(data['lon'], data['lat'])]},
            'properties': {'field': data['value'], 'fillColor': color}
        }

    def create_square(self, lat, lon):
        return [
            [lat + 0.0025, lon + 0.0025],
            [lat + 0.0025, lon - 0.0025],
            [lat - 0.0025, lon - 0.0025],
            [lat - 0.0025, lon + 0.0025],
            [lat + 0.0025, lon + 0.0025]
        ]

    def get_interpolated_list(self):

        interpolated_lst = []
        weather_array = []
        for station in self.station_dict.values():
            if station['latest_data'] != None:
                weather_array.append([station['latest_data']['lon'], station['latest_data']['lat'],
                                      station['latest_data']['value']])

        # Edge Conditions
        if len(weather_array) == 0:
            return None
        elif len(weather_array) == 1:
            return [{
                'lon': weather_array[0][0],
                'lat': weather_array[0][1],
                'value': weather_array[0][2]
            }]

        weather_mat = np.array(weather_array)

        point_mat = weather_mat[:, 0:2]
        value_mat = weather_mat[:, 2]

        self.min_value, self.max_value = min(value_mat), max(value_mat)
        print(self.min_value)
        print(self.max_value)

        lon_max, lon_min = max(weather_mat[:, 0]), min(weather_mat[:, 0])
        lat_max, lat_min = max(weather_mat[:, 1]), min(weather_mat[:, 1])

        width = 2 * int(abs(lon_max - lon_min) / 0.01)
        height = 2 * int(abs(lat_max - lat_min) / 0.01)

        lon_meshed = np.array([[float(val) / 1000.0 for val in range(
            int(lon_min * 1000.0), int(lon_max * 1000.0), 5)] for _ in range(height)])

        lat_meshed = np.column_stack(
            [float(val) / 1000.0 for val in range(int(lat_min * 1000.0), int(lat_max * 1000.0), 5)] for _ in range(width))

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
