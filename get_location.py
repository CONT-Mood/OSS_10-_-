import folium as g
from geopy.geocoders import Nominatim
from pprint import pprint

app = Nominatim(user_agent='tutorial')
station = input("역이름을 입력해주세요(예: 서울역)\n")
location = app.geocode(station)

#역 정보 및 좌표
pprint(location)
pprint(location.point.latitude)
pprint(location.point.longitude)

g_map = g.Map(location=[location.point.latitude, location.point.longitude], zoom_start=18)

marker = g.Marker([location.point.latitude, location.point.longitude],
                  popup='station',
                  icon = g.Icon(color='purple'))

marker.add_to(g_map)

g_map