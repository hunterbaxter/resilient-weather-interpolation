from kafka_tools import KafkaWeather
from pandas import Timestamp


weather_center_names = [
    'Center1',
    'Center2',
    'Center3'
]

kafka = KafkaWeather(weather_center_names, '1.1.1.1.1.2')
