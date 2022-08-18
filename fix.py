import mariadb
import os

CONNECTION = mariadb.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "wassceverse",
    port = 3306
)

CURSOR = CONNECTION.cursor()

with open("Include/img/user-sign-icon-person-symbol-human-avatar-vector-12693195.jpg", 'rb') as input_file:
    ablob = input_file.read()
    sql = "UPDATE student_details SET image = ? WHERE index_number = 01939308943984"
    CURSOR.execute(sql, (mariadb.Binary(ablob),))
    CONNECTION.commit()