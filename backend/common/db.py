import os
import sqlite3

DB_LOCAL_FILE_PATH = "./tanapp.db"

def create_new():
    # Check if the file exists, then delete it
    if os.path.exists(DB_LOCAL_FILE_PATH):
        os.remove(DB_LOCAL_FILE_PATH)
    else:
        print(f"{DB_LOCAL_FILE_PATH} does not exist. Will create a new one")
    
    conn = sqlite3.connect(DB_LOCAL_FILE_PATH)
    cursor = conn.cursor()
    sql_dir = "./assets/sql/"
    sql_asset_files = os.listdir("./assets/sql/")
    for file in sql_asset_files:
        with open(sql_dir+file,"r") as f:
            sql_data = f.read()
            for item in sql_data.split(';'):
                #do each stmt individually to see errors when they occur
                cursor.execute(item+";")
                conn.commit()
    conn.close()


def init(force_create_new:bool):
    if force_create_new:
        create_new()

    conn = sqlite3.connect(DB_LOCAL_FILE_PATH)
    return conn


