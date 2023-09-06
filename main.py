import os

import dotenv
import pymysql

TABLE_NAME = 'users'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
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
        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("abcd", 1234) '
        )
        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("abcd", 1234) '
        )
        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("abcd", 1234) '
        )
        print(result)
    connection.commit()
