import mariadb
db = mariadb.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "wassceverse",
    port = 3306
)

cursor = db.cursor()
cursor.execute("SELECT * FROM registered_schools WHERE ")
schools = []
codes = []
emails = []
for data in cursor:
    schools.append(data[1])
    codes.append(data[4])
    emails.append(data[6])

print(schools)
print(codes)
print(emails)