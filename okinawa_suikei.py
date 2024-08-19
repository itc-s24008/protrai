import requests
from bs4 import BeautifulSoup

uri = 'https://paiza.jp/paijo'
html = requests.get(uri)

soup = BeautifulSoup(html.text, 'html.parser')

backnumber = soup.find('div', class_='p-paijo__backnumber-list--older')

for element in backnumber.find_all('a'):
    print(element['href'])
