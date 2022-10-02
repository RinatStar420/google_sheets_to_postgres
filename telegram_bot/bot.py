import datetime
import requests
from read_sheets.read_sheets import load_google_sheets_to_list


def send_user_message(token, chat_id):
    google_sheets_dict = load_google_sheets_to_list()

    last_day = datetime.date.today()
    msg = ''
    for item in google_sheets_dict:
        if datetime.datetime.strptime(item.get('date_delivery'), '%d.%m.%Y').date() != last_day:
            msg += str(item) + ' - срок поставки истёк\n'
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={str(item) + ' - срок поставки истёк'}"
            requests.get(url).json()
