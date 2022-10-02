from db_postgreSQL.db import DB
from db_postgreSQL.config import db_host, db_user, db_password
from read_sheets.read_sheets import load_google_sheets_to_list

postgres = DB(db_host, db_user, db_password)
postgres.connect_data()
postgres.create_table_orders()
check = load_google_sheets_to_list()
postgres.insert_order_to_orders(check)