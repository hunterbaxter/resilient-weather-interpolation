from kafka_tools import KafkaWeather
from pandas import Timestamp
from apscheduler.schedulers.background import BackgroundScheduler
import time


def dum_func():
    print('Im Dum')


scheduler = BackgroundScheduler()

scheduler.start()

weather_center_names = [
    'Center1',
    'Center2',
    'Center3'
]

time.sleep(30)

kafka = KafkaWeather(weather_center_names, '1.1.1.1.1.2')
