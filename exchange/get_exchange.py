from bs4 import BeautifulSoup as bs
import requests


def get_dollar_exchange(price_usd):
    r = requests.get("https://www.cbr.ru/scripts/XML_daily.asp?")
    soup = bs(r.content, 'xml')
    price = soup.find(ID="R01235").find("Value").text
    return round((float(price.replace(",", ".")) * price_usd), 2)

