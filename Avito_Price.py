import pandas as pd
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

import requests

url = 'https://www.avito.ru/rossiya/avtomobili'
page = requests.get(url)
popular_cars = BeautifulSoup(page.text, 'lxml').find('div', {'class':'popular-rubricator-links-b0HPS'})
cars = {'name': [], 'amount': []}
total_amount = int(BeautifulSoup(page.text, 'lxml').find('span',{'class': 'page-title-count-1oJOc'}).text.replace(' ', ''))
total_sum = 0
for name in popular_cars.find_all('a'):
    cars['name'].append(name.text)
for amount in popular_cars.find_all('span'):
    cnt = int(amount.text.replace(',', ''))
    total_sum += cnt
    cars['amount'].append(cnt)
cars['name'].append('Другие')
cars['amount'].append(total_amount - total_sum)
df = pd.DataFrame(data=cars)
ax = df.plot.bar(x='name', y='amount', legend=False, rot=75, figsize=(14, 5), title='Объявления о продаже автомобилей в России')
ax.set_xlabel("Название")
ax.set_ylabel("Кол-во")
ax.grid(axis='y')
plt.tight_layout()
plt.show()