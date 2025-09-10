import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

source = pd.read_json('Python\ex1\el_data_2024.json')
electricity_data = pd.json_normalize(source['data'])
print(electricity_data.head())

source_data2 = pd.read_csv('Python\ex1\ilm.csv')
weather_data = pd.DataFrame(source_data2)
print(weather_data.head())

weather_data["datetime"] = pd.to_datetime(
    weather_data["Aasta"].astype(str) + "-" +
    weather_data["Kuu"].astype(str) + "-" +
    weather_data["Päev"].astype(str) + " " +
    weather_data["Kell (UTC)"]
)
merged = pd.merge(electricity_data, weather_data, on="datetime", how="inner")
print(merged.head())
