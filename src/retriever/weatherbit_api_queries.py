from datetime import datetime


BASE_URL = "https://api.weatherbit.io/v2.0/"


def current_weather_url(key: str,
                        lat: float,
                        lon: float) -> str:
    return BASE_URL + \
        f"current?lat={lat}&lon={lon}&include=minutely&key={key}"


def historical_weather_url(key: str,
                           lat: float,
                           lon: float,
                           start_date: str,
                           end_date: str,
                           tz: str = "utc",
                           granularity: str = "hourly") -> str:
    # NOTE: There is the option to specify the hour by using YYYY-MM-DD:HH
    verify_date(start_date)
    verify_date(end_date)
    return BASE_URL + \
        f"history/{granularity}?lat={lat}&lon={lon}" + \
        f"&start_date={start_date}&end_date={end_date}&key={key}"


def verify_date(date: str) -> bool:
    format = "%Y-%m-%d"
    return bool(datetime.strptime(date, format))
