from ast import literal_eval as make_tuple
from kafka import KafkaProducer  # producer of events
import pandas as pd
import requests
import logging
from time import sleep
from weatherbit_api_queries import current_weather_url, historical_weather_url


STATION_CSV_PATH = "stations_production.csv"
# NOTE: limitation is due to weatherbit api pricing
CALLS_PER_SECOND = 5


def get_request_weatherbit(key: str,
                           lat: float,
                           lon: float,
                           current: bool = True,
                           start_date: str = None,
                           end_date: str = None):
    if current:
        url = current_weather_url(key=key, lat=lat, lon=lon)
    else:
        url = historical_weather_url(key=key, lat=lat, lon=lon)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Get Request Failed with Status Code {response.status_code}")


def retrieve_and_send_current(ip: str,
                              lat: float,
                              lon: float,
                              key: str) -> None:
    producer = KafkaProducer(bootstrap_servers=f"{ip}:9092", acks=1)
    data = get_request_weatherbit(key, lat, lon)["data"][0]
    producer.send(f"lat{lat}lon{lon}", value=bytes(str(data), 'ascii'))


def retrieve_cycle(ip: str,
                   key: str):
    logging.info("Starting a retrieve cycle")
    # TODO: Dynamically get staions in bounded box
    # columsn are "station_id", and "coordinates" which is lat,lon
    logging.debug("reading stations file")
    stations = pd.read_csv(STATION_CSV_PATH)
    logging.debug("succesfully read stations file")
    # used to ensure we don't go over API limits
    count = 0
    for i in stations["coordinates"]:
        count = count + 1
        if count % CALLS_PER_SECOND == 0:
            sleep(1)
            count = 0
        coordinates = make_tuple(i)
        print(f"lat: {coordinates[0]}")
        print(f"lon: {coordinates[1]}")
        logging.debug(f"retrieving and sending station at {coordinates}")
        retrieve_and_send_current(ip=ip,
                                  lat=coordinates[0],
                                  lon=coordinates[1],
                                  key=key)
    logging.info("Ending a retrieve cycle")
