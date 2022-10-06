from flask import Flask, render_template
from db_postgreSQL.db import DB
from db_postgreSQL.config import db_host, db_user, db_password
from write_sheet_webapp.write_sheets_for_flask import get_value_for_flask
from telegram_bot.bot import send_user_message

app = Flask(__name__)
postgres = DB(db_host, db_user, db_password)

TOKEN = '' # SET TOKEN ID
CHAT_ID = '' # SET CHAT ID


@app.route('/')
def index():
    orders = get_value_for_flask()
    return render_template('index.html', orders=orders)


if __name__ == "__main__":
    send_user_message(TOKEN, CHAT_ID)
    app.run(host='0.0.0.0', port=5000, debug=True)
