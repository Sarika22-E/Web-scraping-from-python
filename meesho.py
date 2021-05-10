import requests
import sys
from bs4 import BeautifulSoup
r = requests.get('https://meesho.com/women-kurtis/pl/dn6ft')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
# costs = soup.find_all('div', {"class": "plp-cost-desktop"})
kurta={}
# for cost in reviews:
#     kurta.update({"price":cost.text})
#     print(kurta)
brand = soup.find_all('h4', {"class": "plp-card-title-desktop"})
costs = soup.find_all('div', {"class": "plp-cost-desktop"})
for i in brand:
    for j in costs:
        kurta.update({i.text:j.text})
print(kurta)
# for names in brand:
#     for cost in costs:
#         kurta.update({brand.text:costs.text})
# print(kurta)   