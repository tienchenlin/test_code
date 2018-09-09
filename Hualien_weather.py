def mod5():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/inc/UVI/Hualien_County.htm?_=\
1536423242592'
    html = requests.get(url).text.encod('utf-8-sig')
    mod = hashlib.md5(html).hexdigest()


import requests,hashlib
from bs4 import BeautifulSoup



url ='https://www.cwb.gov.tw/V7/forecast/taiwan/inc/UVI/Hualien_County.htm?_=\
1536423242592'
html = requests.get(url)
html.encoding = 'UTF-8'
soup = BeautifulSoup(html.text,'html.parser')

data1 = soup.select('#forecast0')
#print(data1)

data2 = data1[0].find_all(['th','td'])
#print(data2)

data3 = data1[0].find_all('img')
#print(data3)
tkdata = dict()

for i in range(8):
    tkdata[data2[i].text] = data2[i+8].text

for key in tkdata.keys():
    print(f"{key:10}, {tkdata[key]:10}")

     
