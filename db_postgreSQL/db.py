import psycopg2
from datetime import datetime
from exchange.get_exchange import get_dollar_exchange


class DB:
    def __init__(self,db_host, db_user, db_password):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password


    def connect_data(self):
        conn = psycopg2.connect(host=self.db_host, user=self.db_user, password=self.db_password)
        conn.autocommit = True
        return conn

    def create_table_memory(self):
        try:
            with self.connect_data().cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE memory(
                     sheet text ARRAY
                     );
                    """
                )
                print("[INFO] Table created")

        except Exception as ex:
            print('[INFO] Error while working with postgreSQL', ex)

    def create_table_orders(self):
        try:
            with self.connect_data().cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE orders(
                     id serial,
                     заказ integer PRIMARY KEY ,
                     стоимостьUSD integer,
                     стоимостьRUB integer,
                     сроки date
                     );
                    """
                )
                print("[INFO] Table created")

        except Exception as ex:
            print('[INFO] Error while working with postgreSQL', ex)


    def insert_order_to_orders(self, sheet_list):
        try:
            self.connect_data().autocommit = False
            with self.connect_data().cursor() as cursor:
                # i = 0
                # max = len(sheet_list)
                # while i <= max:
                for item in sheet_list:
                    order_info = []
                    insert_into_orders = "INSERT INTO orders (заказ, стоимостьUSD, стоимостьRUB, сроки) VALUES(%s,%s,%s,%s)"
                    order_info.append([int(item.get("number_order")), int(item.get('price')), get_dollar_exchange(int(item.get('price'))), datetime.strptime(item.get('date_delivery'), '%d.%m.%Y').strftime('%m.%d.%Y')[:10]])
                    cursor.executemany(insert_into_orders, order_info)
                    print("[INFO] order insert")
                    # i += 1
                # self.connect_data().commit()

        except Exception as ex:
            print('[Error]  insert order', ex)

    def insert_sheet_to_memory(self, sheet_list):
        try:
            self.connect_data().autocommit = False
            with self.connect_data().cursor() as cursor:

                insert_into_memory = f"INSERT INTO memory (sheet) VALUES(ARRAY{sheet_list})"
                cursor.execute(insert_into_memory)
                print("[INFO] memory insert")
                    # self.connect_data().commit()

        except Exception as ex:
            print('[Error]  insert order', ex)

    def select_rows_out_orders(self):
        try:
            with self.connect_data().cursor() as cursor:
                select_out_orders = "SELECT id, заказ, стоимостьUSD, сроки FROM orders"
                cursor.execute(select_out_orders)
                response = cursor.fetchall()
                print("[INFO] select execute")

                return response
        except Exception as ex:
            print('[Error]  select execute', ex)

    def select_rows_out_memory(self):
        try:
            with self.connect_data().cursor() as cursor:
                select_out_memory = "SELECT sheet FROM memory"
                cursor.execute(select_out_memory)
                response = cursor.fetchall()
                print("[INFO] select execute")

                return response
        except Exception as ex:
            print('[Error]  select execute', ex)

    def delete_table_orders(self):
        try:

            with self.connect_data().cursor() as cursor:
                delete_table = "DROP TABLE orders"
                cursor.execute(delete_table)
                print("[INFO] delete execute")

        except Exception as ex:
            print('[Error]  delete execute', ex)

    def delete_table_memory(self):
        try:

            with self.connect_data().cursor() as cursor:
                delete_table = "DROP TABLE memory"
                cursor.execute(delete_table)
                print("[INFO] delete execute")

        except Exception as ex:
            print('[Error]  delete execute', ex)


