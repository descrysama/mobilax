import pymysql
import os
import json
from dotenv import load_dotenv
load_dotenv()

def connect_to_database(host, port, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            port=int(port),
            password=password,
            database=database
        )
        if connection:
            print(json.dumps({'MOBILAX': 'connected to database...'}))
            return connection
    except pymysql.Error as e:
        print("Error connecting to the database:", e)

    return None


def getMobilaxLinks() :
    db_host = os.getenv("MARIADB_HOST")
    db_user = os.getenv("MARIADB_USERNAME")
    db_password = os.getenv("MARIADB_PASSWORD")
    db_database = os.getenv("MARIADB_DATABASE_NAME")
    db_port = os.getenv("MARIADB_PORT")
    db_tablename = os.getenv("MARIADB_TABLENAME")
    connection = connect_to_database(db_host, db_port, db_user, db_password, db_database)
    cursor = connection.cursor()
    query = "SELECT url FROM " + str(db_tablename)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result