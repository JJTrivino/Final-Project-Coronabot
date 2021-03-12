from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify
import sqlite3
from sqlite3 import Error
import pandas as pd
from flask_jsonpify import jsonpify
import os
from flask import send_file

app = Flask(__name__)
app.static_folder = 'static'

chatbot = ChatBot('Murphy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
        read_only=True, #To disable the bot to keep storing each question in memory
        logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.99
        }
    ],
    database_uri='sqlite:///database.sqlite3'
    )

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def emergency ():
    print("Call 112 or call ahead to your local emergency facility")
    os.system("say -v Samantha Call emergencies")
    return print("Ask help")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user = request.args.get('msg')
    alert = ["trouble breathing", "persistent pain", "pressure in the chest", "confusion","inhability to wake",
            "pale", "gray", "blue-colored","help"]
    for x in alert:
        if x in user:
            return emergency()
    return str(chatbot.get_response(user))

@app.route("/brain")
def see_brain():
    create_connection("database.sqlite3")
    cnx = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query("SELECT * FROM statement",cnx)
    df_list = df.values.tolist()
    JSONP_data = jsonpify(df_list)
    return JSONP_data

@app.route("/text")
def column_text():
    create_connection("database.sqlite3")
    cnx = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query("SELECT text FROM statement",cnx)
    df_list = df.values.tolist()
    JSONP_data = (jsonpify(df_list))
    return JSONP_data

@app.route("/Q&A")
def quest():
    cnx = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query("SELECT in_response_to, text FROM statement",cnx)
    df_list = df.values.tolist()
    JSONP_data = (jsonpify(df_list))
    return JSONP_data

@app.route("/fever")
def historical():
    cnx = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query("SELECT in_response_to, text FROM statement",cnx)
    df_list = df.values.tolist()
    JSONP_data = (jsonpify(df_list))
    return JSONP_data


@app.route('/fev')
def get_image():
    filename = 'Ex.jpg'
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    create_connection("database.sqlite3")
    
if __name__ == "__main__":
    app.run() 

