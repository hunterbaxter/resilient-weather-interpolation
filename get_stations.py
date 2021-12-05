import pandas as pd

# NOTE: File downloaded from weatherbit. Would be nice to have it automated.
df = pd.read_csv("stations_stable.csv")
df = df[df["country_code"] == "US"]
df = df[df["frequency"] == "current only"]
LEFT_LONG = -88.00
RIGHT_LONG = -85.00
TOP_LAT = 36.49
BOT_LAT = 35.55
df = df[(BOT_LAT < df["lat"]) & (df["lat"] < TOP_LAT) &
        (LEFT_LONG < df["lon"]) & (df["lon"] < RIGHT_LONG)]
print(f"unique stations in region = {len(df['station_id'].unique())}")
df[["station_id", "lat", "lon"]].to_csv("stations_production.csv", index=False)
df[["station_id", "lat", "lon"]] \
    .head(2).to_csv("stations_test.csv", index=False)
