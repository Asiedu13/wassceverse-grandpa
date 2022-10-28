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

sql = "SELECT * FROM student_details WHERE school = ?"
CURSOR.execute(sql, ("Presbyterian Boys' Secondary School",))
data = []
for d in CURSOR:
    data.append(d)
print(data)