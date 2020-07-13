import folium
import pandas
import json

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
volnm = list(data['NAME'])


def elev_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='My Map')
for lt, ln, el, vnm in zip(lat, lon, elev, volnm):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                                     popup=vnm + ' ' + str(el) + 'm', fill_color=elev_color(el), color='grey', fill_opacity=0.7))
map.add_child(fg)

map.save("MapUno.html")
