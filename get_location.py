import folium as g
from geopy.geocoders import Nominatim
from pprint import pprint

app = Nominatim(user_agent='tutorial')
location = app.geocode('서울역')
pprint(location)

pprint(location.point.latitude)
pprint(location.point.longitude)

g_map = g.Map(location=[location.point.latitude, location.point.longitude], zoom_start=18)

marker = g.Marker([location.point.latitude, location.point.longitude],
                  popup='station',
                  icon = g.Icon(color='purple'))

marker.add_to(g_map)

g_map