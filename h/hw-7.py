import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')


def insert_product(connection, product):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES
        (?, ?, ?) 
        '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCT function')


def update_price_product(connection, product):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE_PRODUCT function')


def update_quantity_product(connection, product):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY_PRODUCT function')


def delete_product(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_PRODUCT function')


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL_PRODUCT function')


def select_products_by_price_and_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products 
        WHERE price <= ?  AND quantity >= ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_PRODUCT_BY function')


def select_products_by_name(connection):
    try:
        sql = '''SELECT * FROM products 
        WHERE product_title LIKE '%Kurut%'
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_PRODUCT_BY_NAME function')


sql_to_creates_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


my_connection = create_connection('hw.db')
if my_connection:
    print('Connected successfully!')
    # create_table(my_connection, sql_to_creates_products_table)
    # insert_product(my_connection, ('Classic Chocolate', 120.50, 7))
    # insert_product(my_connection, ('Milk Chocolate', 129.99, 3))
    # insert_product(my_connection, ('White Chocolate', 99.99, 10))
    # insert_product(my_connection, ('Black Chocolate', 150.40, 8))
    # insert_product(my_connection, ('Salted Chocolate', 145.50, 5))
    # insert_product(my_connection, ('Classic Marmalade', 89.90, 12))
    # insert_product(my_connection, ('Berry Marmalade', 100.00, 10))
    # insert_product(my_connection, ('Fruit Marmalade', 100.00, 7))
    # insert_product(my_connection, ('Classic Kurut', 30.30, 15))
    # insert_product(my_connection, ('Smoked Kurut', 35.50, 4))
    # insert_product(my_connection, ('Mint Gum', 45.80, 9))
    # insert_product(my_connection, ('Fruit Gum', 43.30, 3))
    # insert_product(my_connection, ('Cheese Chips', 150.70, 4))
    # insert_product(my_connection, ('Spicy Chips', 145.99, 7))
    # insert_product(my_connection, ('Salted Chips', 120.00, 2))
    # update_price_product(my_connection, (200, 1))
    # update_quantity_product(my_connection, (15, 11))
    # delete_product(my_connection, 1)
    # select_all_products(my_connection)
    # select_products_by_price_and_quantity(my_connection, (90, 3))
    # select_products_by_name(my_connection)
    my_connection.close()
