import mysql.connector

__cnx = None

def get_sql_connection():
    __cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='gs')
    return __cnx