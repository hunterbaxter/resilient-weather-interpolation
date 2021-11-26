from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
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


def convert_time(timestamp):
    # TODO: write test to catch error if wrong format or unit

    # NOTE: if one wants to use non-unix field
    # t = pd.to_datetime(timestamp,
    #                    format="%Y-%m-%d %H:%M")
    return pd.to_datetime(timestamp, unit='s', utc=True)


def retrieve_and_send_current(host_url: str,
                              token: str,
                              org: str,
                              bucket: str,
                              key: str,
                              lat: float,
                              lon: float) -> None:
    client = InfluxDBClient(url=host_url,
                            token=token,
                            org=org)
    # TODO: Explore performance options here
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # TODO: Confirm that bucket parameter is actually a bucket in client
    # NOTE: See documentation for why data is retrieved like this
    data = get_request_weatherbit(key, lat, lon)["data"][0]
    record = []
    try:
        record.append({
            "measurement": "weather",
            "tags": {
                "lat": data['lat'],
                "lon": data['lon']
            },
            # TODO: Need to resolve timezone issues - this is the last value
            "time": convert_time(data['ts']),
            "fields": {
                'wind_cdir': data['wind_cdir'],
                'rh': float(data['rh']),
                'pod': data['pod'],
                'pres': float(data['pres']),
                'timezone': data['timezone'],
                'country_code': data['country_code'],
                'clouds': float(data['clouds']),
                'vis': float(data['vis']),
                'wind_spd': float(data['wind_spd']),
                'wind_cdir_full': data['wind_cdir_full'],
                'app_temp': float(data['app_temp']),
                'state_code': data['state_code'],
                'h_angle': float(data['h_angle']),
                'dewpt': float(data['dewpt']),
                'weather_icon': data['weather']["icon"],
                'weather_code': int(data['weather']["code"]),
                'weather_description': data['weather']["description"],
                'uv': float(data['uv']),
                'aqi': float(data['aqi']),
                # TODO: Find a list of stations in nashville with their lat/lon
                'station': data['station'],
                'wind_dir': float(data['wind_dir']),
                'elev_angle': float(data['elev_angle']),
                'precip': float(data['precip']),
                'ghi': float(data['ghi']),
                'dni': float(data['dni']),
                'dhi': float(data['dhi']),
                'solar_rad': float(data['solar_rad']),
                'city_name': data['city_name'],
                'sunrise': data['sunrise'],
                'sunset': data['sunset'],
                'temp': float(data['temp']),
                'slp': float(data['slp']),
            }
        })
    except Exception as e:
        print(f"ERROR: {e}")
    write_api.write(bucket=bucket, record=record)
