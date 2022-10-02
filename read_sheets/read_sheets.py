import httplib2


from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials





def load_google_sheets_to_list():
    """Функция чтения таблицы, которой выдан доступ
    для сервисного аккаунта"""

    ID_SHEETS = '1B6GXrawHiA4AHc5dlMFhYUVeCO-QJGWDTOZ5YQfnb7s'
    credentials_json = "./config/creds.json"
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_json,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=httpAuth)
    values = service.spreadsheets().values().get(
        spreadsheetId=ID_SHEETS,
        range='A:D',
        majorDimension='ROWS'
    ).execute()
    google_sheets = [dict(zip(['id', 'number_order', 'price', 'date_delivery'], l)) for l in values.get('values')[1:]]
    return google_sheets




