import time

from db_postgreSQL.db import DB
from db_postgreSQL.config import db_host, db_user, db_password
from read_sheets.read_sheets import load_google_sheets_to_list
from write_sheet_webapp.write_sheets_for_flask import get_value_for_flask



def get_value_for_memory():
    sheet_list = load_google_sheets_to_list()
    memory = []
    for item in sheet_list:
        memory.append([item.get("id"), item.get("number_order"), item.get('price')])
    return memory

def check_update():
    postgres = DB(db_host, db_user, db_password)
    postgres.create_table_memory()
    sheet_list = get_value_for_flask()
    postgres.insert_order_to_orders(sheet_list)
    while True:
        memory = postgres.select_rows_out_memory()[0]
        memory_list = memory[0]
        if get_value_for_flask() != memory_list:
            postgres.delete_table_orders()
            postgres.delete_table_memory()
            postgres.create_table_orders()
            postgres.create_table_memory()
            postgres.insert_order_to_orders(sheet_list)
            postgres.insert_sheet_to_memory(sheet_list)
        else:
            pass
        time.sleep(5)
