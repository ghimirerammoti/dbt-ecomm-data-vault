import pandas as pd
from geopy.geocoders import Nominatim  
import time
import requests
from datetime import datetime
from sqlalchemy import create_engine
import os

db_user=os.getenv("DB_USER")
db_user_password=os.getenv("DB_USER_PASSWORD")

url = "https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv"

df=pd.read_csv(url)
print("here is the data")

# Filter for Nepal
nepal_cities = df[df['country'] == 'Nepal']
print(nepal_cities)


geolocator = Nominatim(user_agent="nepal-weather-app")
lat_lon_list = []

for city in nepal_cities['name'].unique():
    try:
        location = geolocator.geocode(f"{city}, Nepal")
        if location:
            lat_lon_list.append({
                'city': city,
                'latitude': location.latitude,
                'longitude': location.longitude
            })
        time.sleep(1)  # to respect rate limits
    except:
        continue

geo_df = pd.DataFrame(lat_lon_list)
print(geo_df)

weather_data = []

'''
for _,row in geo_df.iterrows():
    lat, lon, city = row['latitude'], row['longitude'], row['city']
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(url)
    
    if res.status_code == 200:
        weather = res.json().get('current_weather', {})
        if weather:
            weather_data.append({
                'city': city,
                'latitude': lat,
                'longitude': lon,
                'temperature': weather['temperature'],
                'windspeed': weather['windspeed'],
                'weathercode': weather['weathercode'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

weather_df = pd.DataFrame(weather_data)
engine = create_engine("postgresql://postgres:postgres@localhost:5433/dv")
weather_df.to_sql(name='nepal_weather', con=engine, schema='reporting',if_exists='append', index=False)
'''

for _,row in geo_df.iterrows():
    lat, lon, city = row['latitude'], row['longitude'], row['city']
    # Fetching historical weather data for the next two years
    #url = f"http://historical-forecast-api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date=2023-07-21&end_date=2025-07-26&hourly=temperature_2m,precipitation,dew_point_2m,wind_speed_2m,weather_code,soil_temperature_54cm,soil_moisture_0_to_1cm,relative_humidity_2m,wind_direction_2m,rain,showers,snowfall,cloudcover"
    # Using the Open Meteo API to fetch hourly weather data for today and the next next week
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date=2025-07-21&end_date=2025-07-26&hourly=temperature_2m,precipitation,dew_point_2m,wind_speed_2m,weather_code,soil_temperature_54cm,soil_moisture_0_to_1cm,relative_humidity_2m,wind_direction_2m,rain,showers,snowfall,cloudcover"
    res = requests.get(url)
    #print(res.json())
    
    
    if res.status_code == 200:
        weather = res.json().get('hourly', {})
        if weather:
            for i in range(len(weather['time'])):
                # Extracting the weather data for each timestamp
                weather_data.append({
                    'city': city,
                    'latitude': lat,
                    'longitude': lon,
                    'temperature': weather['temperature_2m'][i],
                    'weathercode': weather['weather_code'][i],
                    'timestamp': weather['time'][i],
                    'precipitation': weather['precipitation'][i],
                    'dew_point': weather['dew_point_2m'][i],
                    'wind_speed': weather['wind_speed_2m'][i],
                    'soil_temperature': weather['soil_temperature_54cm'][i],
                    'soil_moisture': weather['soil_moisture_0_to_1cm'][i],
                    'relative_humidity': weather['relative_humidity_2m'][i],
                    'wind_direction': weather['wind_direction_2m'][i],
                    'rain': weather['rain'][i],
                    'showers': weather['showers'][i],
                    'snowfall': weather['snowfall'][i],
                    'cloudcover': weather['cloudcover'][i]
                })
    else :
        print(f"Failed to fetch data for {city}: {res.status_code}")    
weather_df = pd.DataFrame(weather_data)
#print(weather_df)
engine = create_engine("postgresql://postgres:postgres@localhost:5433/dv")
weather_df.to_sql(name='nepal_weather', con=engine, schema='reporting',if_exists='append', index=False)
