# [Weatherbit](https://www.weatherbit.io/features)
- Weatherbit is a weather data vendor
- Offers [multiple data plans](https://www.weatherbit.io/pricing), but we will probably only need free or starter subsription
- Multiple APIs, both current, and historical.

# What data will we use?
- [Current Weather API](https://www.weatherbit.io/api/weather-current):
    - Challenge: weather data updates every 5-30 minutes based on station reporting frequency
- [Historical Weather API (Sub-Hourly)](https://www.weatherbit.io/api/weather-history-subhourly)
    - Updates every 15 minute interval for any location
    - This surprised me, but one can atually get history by latitude and longitute (I don't know how they do this)
    - TODO: Find out how they go about getting latitude and longitude (nearest station, kriging, etc)


## How does weatherbit get there data?
Data sources for current weather API include [METAR reporting stations](https://www.aviationweather.gov/metar), and data from the [NOAA Meteorological Assimilation Data Ingest System](https://madis.ncep.noaa.gov/)

## Best Practices
- For real time data, use [Current Weather API](https://www.weatherbit.io/api/weather-current), however, Weatherbit recommends one doesnot archive this data, and instead uses a longer-term option like subhourly or historical weather API

# Current Weather API Quirks
- Response is currently 3 identical blobs?
- When one takes the json of the response, the data is a list of lenghth 1 with a dictionary inside of it.
- Example json response:
```
{
   "data":[
      {
         "wind_cdir":"NE",
         "rh":59,
         "pod":"d",
         "lon":"-78.63861",
         "pres":1006.6,
         "timezone":"America\/New_York",
         "ob_time":"2017-08-28 16:45",
         "country_code":"US",
         "clouds":75,
         "vis":10,
         "wind_spd":6.17,
         "wind_cdir_full":"northeast",
         "app_temp":24.25,
         "state_code":"NC",
         "ts":1503936000,
         "h_angle":0,
         "dewpt":15.65,
         "weather":{
            "icon":"c03d",
            "code": 803,
            "description":"Broken clouds"
         },
         "uv":2,
         "aqi":45,
         "station":"CMVN7",
         "wind_dir":50,
         "elev_angle":63,
         "datetime":"2017-08-28:17",
         "precip":0,
         "ghi":444.4,
         "dni":500,
         "dhi":120,
         "solar_rad":350,
         "city_name":"Raleigh",
         "sunrise":"10:44",
         "sunset":"23:47",
         "temp":24.19,
         "lat":"35.7721",
         "slp":1022.2
      }
   ],
   "minutely":[ ... ],
   "count":1
}
```
