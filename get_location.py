import pandas as pd
from openpyxl import load_workbook
from haversine import haversine
import folium
from geopy.geocoders import Nominatim
from pprint import pprint

app = Nominatim(user_agent='tutorial')
station = input("역이름을 입력해주세요(예: 서울역)\n")
location = app.geocode(station)

# 수도권 지하철 정보 엑셀 파일 가져옴
df = pd.read_excel("지하철좌표.xlsx", engine = "openpyxl")

g_map = folium.Map(location=[location.point.latitude, location.point.longitude], zoom_start=18)

# 찾고자 하는 역을 파란색으로 마커 표시
marker = folium.Marker([location.point.latitude, location.point.longitude],
                  popup='station',
                  icon = folium.Icon(color='blue'))
marker.add_to(g_map)

# 주변 역 표시
for i in range(0, 589):
    start = (location.point.latitude, location.point.longitude)
    goal = (df.loc[i]['위도'], df.loc[i]['경도'])
    dis = haversine(start, goal)
    # 주변 약 1킬로미터 역들을 보라색으로 표시
    if(dis <= 1) :
      close_marker = folium.Marker([df.loc[i]['위도'], df.loc[i]['경도']],
                popup='close_station',
                icon = folium.Icon(color='purple'))
      close_marker.add_to(g_map)

g_map