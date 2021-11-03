import pandas as pd 
from openpyxl import load_workbook
from haversine import haversine
import folium as g
from geopy.geocoders import Nominatim
from pprint import pprint

app = Nominatim(user_agent='tutorial')
station = input("역이름을 입력해주세요(예: 서울역)\n")
location = app.geocode(station)

df = pd.read_excel("지하철좌표.xlsx", engine = "openpyxl")
for i in range(0, 589):
    start = (location.point.latitude, location.point.longitude)
    goal = (df.loc[[i], :]['위도'], df.loc[[i], :]['경도'])
    dis = haversine(start, goal)
    if(dis <= 2) :
        print(df.loc[i]['역이름'])
#        location2 = app.geocode(str(df.loc[i]['역이름'])+'역')
#        g_map = g.Map(location2=[location2.point.latitude, location2.point.longitude], zoom_start=18)
#        marker = g.Marker([location2.point.latitude, location2.point.longitude], popup='station', icon = g.Icon(color='purple'))
#        marker.add_to(g_map)
        

