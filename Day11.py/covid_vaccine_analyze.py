import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date, datetime, time, timezone
import folium
import json

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\covid-vaccination-doses-per-capita.csv")
print(df.info())

df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)

print(df.head())

len(df["Entity"].unique())
covid_c = df.groupby(["Entity"])

# Separate the information of the created group by key and print them.
for key, group in covid_c:
    print('+key:', key)
    print('+number:', len(group))
    print(group.head())
    print('\n')

total_df = covid_c[['Cumulative COVID-19 vaccinations per 100 people']].sum()

total_df.columns = ['total_vaccinations_per_hundred']

print(total_df.head())

# Basic Map
basic_map = folium.Map(
    location=[12.828388886497882, 80.04553326073784],
    zoom_start=13,
    tiles="OpenStreetMap"
)

basic_map.save("map.html")

print("Basic map saved as map.html")

# Marker Map
marker_map = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles="OpenStreetMap"
)

folium.Marker(
    location=[45.3288, -121.6625],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(marker_map)

folium.Marker(
    location=[45.3311, -121.7113],
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(marker_map)

folium.CircleMarker(
    location=[45.3800, -121.6000],
    radius=100,
    popup="circle",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(marker_map)

marker_map.save("marker_map.html")

print("Marker map saved as marker_map.html")

# Choropleth Map
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)

state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"

state_data = pd.read_csv(state_unemployment)

choropleth_map = folium.Map(
    location=[48, -102],
    zoom_start=3
)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(choropleth_map)

folium.LayerControl().add_to(choropleth_map)

choropleth_map.save("us_unemployment_map.html")

print("Choropleth map saved as us_unemployment_map.html")


center = [35.762887375145795, 84.08313219586536]

m = folium.Map(
    location=center,
    zoom_start=2,
    max_bounds=True,
    min_zoom=1,
    min_lat=-84,
    max_lat=84,
    min_lon=-175,
    max_lon=187
)

geo_path = r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\countries.geojson"

json_data = json.load(open(geo_path, encoding='utf-8'))

folium.Choropleth(
    geo_data=json_data,
    data=total_df,
    columns=(total_df.index, 'total_vaccinations_per_hundred'),
    key_on='properties.name',
    fill_color='RdYlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
).add_to(m)

folium.LayerControl().add_to(m)

m.save("world_vaccination_map.html")

print("World vaccination map saved successfully!")