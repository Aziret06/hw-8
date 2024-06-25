
import sqlite3


def get_stores(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT store_id, title FROM store''')
        sts = cursor.fetchall()
        return sts
    except sqlite3.Error as e:
        print(e)
        return []


def get_products(connection, str_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT products.title,
            products.unit_price,
            products.stock_quantity,
            categories.title 
            FROM products
            JOIN categories ON products.category_code = categories.code
            WHERE products.store_id = ?
            ''', (str_id,))
        sts = cursor.fetchall()
        return sts
    except sqlite3.Error as e:
        print(e)


conn = sqlite3.connect('DopUrok.db')
if conn:
    print('Connected to database.')

    stores = get_stores(conn)

    print('Вы можете отобразить список продуктов по выбранному id магазина из'
          'перечня магазинов ниже, для выхода из программы введите цифру 0:')
    for store in stores:
        print(f'{store[0]}. {store[1]}')

    while True:
        store_id = input('Enter the store id: ')
        if store_id == '0':
            print('THE END')
            break
        elif store_id > '3' or store_id < '0':
            print('\nThere is no store with this id. Try again.\n')
        else:
            store_id = int(store_id)
            products = get_products(conn, store_id)
            print('\nList of products in the selected store:\n')
            for product in products:
                print(
                    f'PRODUCT NAME: {product[0]}, '
                    f'PRODUCT PRICE: {product[1]},'
                    f' PRODUCT QUANTITY: {product[2]}, '
                    f'PRODUCT CATEGORY: {product[3]}'
                )
            print()

    conn.close()
else:
    print('Failed to connect to database.')
