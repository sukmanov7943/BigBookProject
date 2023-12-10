import random

from bs4 import BeautifulSoup
import requests
import lxml
import csv
import json
import time
url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

req = requests.get(url,headers)
src = req.text

with open('page.html','w',encoding='utf-8') as file:
    file.write(src)

with open('page.html','r',encoding='utf-8') as file:
    page = file.read()


soup = BeautifulSoup(page,'lxml')
all_products_dict = {}
all_products_href = soup.find_all(class_='mzr-tc-group-item-href')
for item in all_products_href:
    all_products_dict[item.text] = 'https://health-diet.ru' + item.get('href')

with open('all_products_dict.json','w',encoding='utf-8') as file:
   file.write(json.dumps(all_products_dict,indent=4,ensure_ascii=False))
with open('all_products_dict.json','r',encoding='utf-8') as file:
    all_categories=json.load(file)

itearation = int(len(all_categories))-1
count = 0
for name,herf_name in all_categories.items():
        req = requests.get(url=herf_name,headers=headers)
        src = req.text

        with open(f'data/{count}_{name}.html','w',encoding='utf-8') as file:
            file.write(src)
        with open(f'data/{count}_{name}.html','r',encoding='utf-8') as file:
            src = file.read()


        soup = BeautifulSoup(src,'lxml')
        #проверка старницы на пустоту
        alert_page=soup.find(class_='uk-alert-danger')
        if alert_page is not None:
            continue
        characters = soup.find(class_='mzr-tc-group-table').find_all('th')
        product  = characters[0].text
        calories = characters[1].text
        proteins= characters[2].text
        fat = characters[3].text
        carbonades = characters[4].text

        with open(f'data/{count}_{name}.csv','w',encoding='utf-8-sig') as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerow((product,calories,proteins,fat,carbonades))
        product_info = []
        product_data=soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
        for item in product_data:
            product_tds = item.find_all('td')
            title = product_tds[0].find('a').text
            calories=product_tds[1].text
            proteins=product_tds[2].text
            fat = product_tds[3].text
            carbonades=product_tds[4].text

            product_info.append({'Название': title,'Калории': calories,'Белки': proteins,'Жиры': fat,'Углеводы': carbonades})

            with open(f'data/{count}_{name}.csv', 'a', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';',lineterminator='\n')
                writer.writerow((title, calories, proteins, fat, carbonades))

            with open(f'data/{count}_{name}.json','w',encoding='utf-8') as file:
                file.write(json.dumps(product_info,indent=4,ensure_ascii=False))
        count+=1
        print(f'# Итерация № {count}. {name} записан')
        itearation=itearation-1
        if itearation ==0:
            print('Финиш')
            break
        print(f'Осталось итераций: {itearation}')
