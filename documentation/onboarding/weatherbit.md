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

