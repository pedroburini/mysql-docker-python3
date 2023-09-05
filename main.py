import pymysql

connection = pymysql.connect(
    host='localhost',
    user='user',
    password='password',
    database='database',
)

with connection:
    with connection.cursor() as cursor:
        # sql
        print(cursor)
