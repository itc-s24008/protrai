# s24008
# 沖縄県の推計人口のページより最新情報をスクレイピングするPythonコード
# http://ww.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'http://ww.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)
html.encoding = 'shift_JIS'

print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

print(soup.find('title').string)

table = soup.find('table', class_='table1 font2 gyo5')
print(table)

if '人' == id.get_text()

a = []

a.append(1400000)
a.append(700000)
a.append(700000)

print('仮出力')
print('総人口:(a[0])')
print('男:(a[1])人')
print('女:(a[2])人')
