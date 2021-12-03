import pandas as pd


def point_in_tn(lat: float, lon: float) -> bool:
    LEFT_LONG_TN = -90.5
    RIGHT_LONG_TN = -81.5
    TOP_LAT_TN = 36.7
    BOT_LAT_TN = 34.9
    if (BOT_LAT_TN < lat < TOP_LAT_TN) and (LEFT_LONG_TN < lon < RIGHT_LONG_TN):
        return True
    else:
        return False


df = pd.read_csv("stations_stable.csv")
df = df[df["country_code"] == "US"]
df = df[df["frequency"] == "current only"]
LEFT_LONG_TN = -90.5
RIGHT_LONG_TN = -81.5
TOP_LAT_TN = 36.7
BOT_LAT_TN = 34.9
df = df[(BOT_LAT_TN < df["lat"]) & (df["lat"] < TOP_LAT_TN) &
        (LEFT_LONG_TN < df["lon"]) & (df["lon"] < RIGHT_LONG_TN)]
print(f"unique stations in TN = {len(df['station_id'].unique())}")
