from bs4 import BeautifulSoup
import requests
import datetime

current_datetime = datetime.datetime.now()

formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  
  
  return rate

print(formatted_datetime)
print("USD conversion: ")
print(str(get_currency('USD', 'JPY')))
print(str(get_currency('USD', 'KRW')))
print(str(get_currency('USD', 'PHP')))
