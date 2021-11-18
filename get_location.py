import pandas as pd
from requests import get
from haversine import haversine
import folium
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.seoulmetro.co.kr/kr/page.do?menuIdx=366#none')
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'tbl-type1 t-col'})

data1 = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data1.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_2")
data2 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data2.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_3")
data3 = []

for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data3.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_4")
data4 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data4.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_5")
data5 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data5.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_6")
data6 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data6.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_7")
data7 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data7.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_8")
data8 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data8.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

div = soup.find('div', {'class': 'tbl-box1 m-top20'}, id="line_9")
data9 = []
for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0

    for td in tds:
        if (tempnumber % 9 == 0):
            name = tds[0].text
            elebator = tds[1].text
            escalator = tds[2].text
            level_walker = tds[3].text
            wheelchair_lift = tds[4].text
            removable_safety_platform = tds[5].text
            electric_wheelchair_fast_charger = tds[6].text
            disabled_toilet = tds[7].text
            voice_inducer = tds[8].text

            data9.append([name,
                          elebator,
                          escalator,
                          level_walker,
                          wheelchair_lift,
                          removable_safety_platform,
                          electric_wheelchair_fast_charger,
                          disabled_toilet,
                          voice_inducer
                          ])
            tempnumber = tempnumber + 1

print("1번:엘리베이터 2번:에스컬레이터 3번:수평보행기 4번:휠체어리프트 5번:이동식 안전발판 6번:전동휠체어 급속 충전기 7번:장애인 화장실 8번:음성유도기\n")
num = input("필요한 편의시설 번호를 입력하세요 : \n")
ss = ["엘리베이터", "에스컬레이터", "수평보행기", "휠체어리프트", "전동휠체어 급속 충전기", "장애인 화장실", "음성유도기"]

# 지하철 좌표 관련 정보를 받아옴
with open("station_coordinate.xlsx", "wb") as file:
    response = get(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5YJBdpmwJ48OhkNGbR6rXXRazYR0ibIFI4nuxuIgQaWu-LUU2QXK5fqcYAR7kBg91RZRexFI-XMo-/pub?output=xlsx")
    file.write(response.content)

# 역이름과 호선을 받아서 찾아냄
app = Nominatim(user_agent='tutorial')
station_number = input("\n몇 호선인가요?(숫자만 입력해주세요.)\n")
station_number = int(station_number)
station = input("\n역이름을 입력해주세요(예: 서울역)\n")


# 입력받은 역이름 호선을 이용하여 필요한 정보만을 추출함(1~9호선만 존재)
def find_info(station, station_number):
    if (station_number == 1):
        for i in range(0, len(data1)):
            if (data1[i][0] == station):
                return data1[i]
    elif (station_number == 2):
        for i in range(0, len(data2)):
            if (data2[i][0] == station):
                return data2[i]
    elif (station_number == 3):
        for i in range(0, len(data3)):
            if (data3[i][0] == station):
                return data3[i]
    elif (station_number == 4):
        for i in range(0, len(data4)):
            if (data4[i][0] == station):
                return data4[i]
    elif (station_number == 5):
        for i in range(0, len(data5)):
            if (data5[i][0] == station):
                return data5[i]
    elif (station_number == 6):
        for i in range(0, len(data6)):
            if (data6[i][0] == station):
                return data6[i]
    elif (station_number == 7):
        for i in range(0, len(data7)):
            if (data7[i][0] == station):
                return data7[i]
    elif (station_number == 8):
        for i in range(0, len(data8)):
            if (data8[i][0] == station):
                return data8[i]
    elif (station_number == 9):
        for i in range(0, len(data9)):
            if (data9[i][0] == station):
                return data9[i]


station_info = find_info(station, station_number)
location = app.geocode(station)

# 수도권 지하철 정보 엑셀 파일 가져옴
df = pd.read_excel('station_coordinate.xlsx', engine="openpyxl")
# 구글맵을 불러옴
g_map = folium.Map(location=[location.point.latitude, location.point.longitude], zoom_start=15)

# 찾고자 하는 역을 파란색으로 마커 표시
if (station_info is not None) & (station_info[int(num)] != ''):
    marker = folium.Marker([location.point.latitude, location.point.longitude],
                           popup="<pre>" + ss[int(num) - 1] + station_info[int(num)] + "개</pre>",
                           icon=folium.Icon(color='blue'))
    marker.add_to(g_map)
else:
    marker = folium.Marker([location.point.latitude, location.point.longitude],
                           popup="<pre>" + ss[int(num) - 1] + "0개</pre>",
                           icon=folium.Icon(color='blue'))
    marker.add_to(g_map)

# 주변 역 표시
for i in range(1, 439):
    start = (location.point.latitude, location.point.longitude)
    goal = (df.loc[i]['lat'], df.loc[i]['lng'])
    dis = haversine(start, goal)
    # 주변 약 1킬로미터 역들을 보라색으로 표시
    if (dis <= 1.5):
        line = int(df.loc[i]['line'][1:2])
        station_info = find_info(df.loc[i]['name'], line)
        if station_info is not None:
            close_marker = folium.Marker([df.loc[i]['lat'], df.loc[i]['lng']],
                                         popup="<pre>" + ss[int(num) - 1] + station_info[int(num)] + "개</pre>",
                                         icon=folium.Icon(color='purple'))

            close_marker.add_to(g_map)

g_map