from kafka_tools import KafkaWeather
from pandas import Timestamp
from apscheduler.schedulers.background import BackgroundScheduler
import time


weather_center_names = [
    'center1',
    'center2',
    'center3'
]


kafka = KafkaWeather(weather_center_names, '1.1.1.1.1.2')

print(kafka.get_GeoJSON_data())

# print(kafka.get_interpolated_list())
