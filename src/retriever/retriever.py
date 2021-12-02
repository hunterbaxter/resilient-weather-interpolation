from kafka import KafkaProducer  # producer of events
import requests
from .weatherbit_api_queries import current_weather_url, historical_weather_url


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
                              key: str,
                              lat: float,
                              lon: float) -> None:
    producer = KafkaProducer(bootstrap_servers=f"{ip}:9092", acks=1)
    # data = get_request_weatherbit(key, lat, lon)["data"][0]
    data = "hi"
    producer.send(f"lat{lat}lon{lon}", value=bytes(str(data), 'ascii'))
