import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image

def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    return conn

def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = """UPDATE student_details
        SET image = ?
        WHERE _rowid_ = 2"""
        conn.execute(sql,[sqlite3.Binary(ablob)]) 
        conn.commit()


conn = create_or_open_db('server.db')
picture_file = "C:/Users/FUJITSU/Desktop/faces/edited/face6.jpg.png"
insert_picture(conn, picture_file)
conn.close()
