import requests
from bs4 import BeautifulSoup


response = requests.get('http://www.seoulmetro.co.kr/kr/page.do?menuIdx=366#none')
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', { 'class': 'tbl-type1 t-col'})
# 1호선 관련 테이블 찾음? 맞나 이게

data1 = []


for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        
            print("\n\n")

print(data1)
print("\n\n")

div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_2")
    

data2 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data2)
print("\n\n")

div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_3")
    

data3 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data3)
print("\n\n")

div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_4")
    

data4 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data4)
print("\n\n")

div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_5")
    

data5 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data5)
print("\n\n")

div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_6")
    

data6 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data6)
print("\n\n")


div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_7")
    

data7 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data7)
print("\n\n")



div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_8")
    

data8 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data8)
print("\n\n")


div = soup.find('div', { 'class': 'tbl-box1 m-top20'}, id="line_9")
    

data9 = []


for tr in div.find_all('tr'):
    tds = list(tr.find_all('td'))
    tempnumber = 0
    
    for td in tds:
        if (tempnumber%9 == 0):
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
        

print(data9)
print("\n\n")



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        