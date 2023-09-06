import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'users'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # caution: this clears table
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME} ')
    connection.commit()

    # start to manipulate data from here
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%s, %s) '
        )
        data = ('abcd', 1234)
        result = cursor.execute(sql, data)
        """ print(sql, data)
        print(result) """
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%(name)s, %(age)s) '
        )
        data2 = {
            "name": "efgh",
            "age": 5678,
        }
        result = cursor.execute(sql, data2)
        """ print(sql)
        print(data2)
        print(result) """
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "ijkl", "age": 91011, },
            {"name": "mnop", "age": 1213, },
            {"name": "qwerty", "age": 1415, },
        )
        result = cursor.executemany(sql, data3)
        """ print(sql)
        print(data3)
        print(result) """
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%s, %s) '
        )
        data4 = (
            ("asdas", 2145),
            ("fsaff", 1256),
        )
        result = cursor.executemany(sql, data4)
        """ print(sql)
        print(data4)
        print(result) """
    connection.commit()

    # reading values with select
    with connection.cursor() as cursor:
        """ min_id = int(input('min id: '))
        max_id = int(input('max id: ')) """
        min_id = 2
        max_id = 4

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (min_id, max_id))
        # print(cursor.mogrify(sql, (min_id, max_id)))
        data5 = cursor.fetchall()

        """ for row in data5:
            print(row) """

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        print(cursor.execute(sql, (4,)))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        """ for row in cursor.fetchall():
            print(row) """

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('adsdsava', 1245661, 5))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        """ for row in cursor.fetchall():
            _id, name, age = row
            print(_id, name, age) """

        for row in cursor.fetchall():
            print(row)
    connection.commit()
