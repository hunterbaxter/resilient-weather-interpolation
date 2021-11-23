import pytest


from src.retriever.weatherbit_api_queries import get_current_weather, \
    get_historical_weather


def test_get_historical_weather():
    key = "test_key"
    lat = 36.131687
    lon = -86.668823
    valid_start = "2021-01-01"
    valid_end = "2021-02-02"
    assert get_historical_weather(key=key,
                                  lat=lat,
                                  lon=lon,
                                  start_date=valid_start,
                                  end_date=valid_end) \
        == f"https://api.weatherbit.io/v2.0/history/hourly?lat={lat}&lon={lon}&start_date={valid_start}&end_date={valid_end}&key={key}"

    invalid_start = "01-01-2021"
    invalid_end = "01-01-2021"
    with pytest.raises(ValueError):
        get_historical_weather(key=key,
                               lat=lat,
                               lon=lon,
                               start_date=invalid_start,
                               end_date=invalid_end)


def test_get_current_weather():
    key = "test_key"
    lat = 36.131687
    lon = -86.668823
    assert get_current_weather(key=key,
                               lat=lat,
                               lon=lon) \
    == f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&include=minutely&key=test_key"
