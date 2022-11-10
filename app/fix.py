import mariadb

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(photo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mariadb.connect(
            host="localhost",
            user="root",
            passwd="",
            database="wassceverse",
            port=3306
        )
        cursor = connection.cursor()
        sql_insert_blob_query = """UPDATE registered_schools SET school_logo = ? WHERE id = 1"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (empPicture,)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))


insertBLOB("download.png")