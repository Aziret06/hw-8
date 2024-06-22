
import sqlite3


def get_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT id, title FROM cities''')
        cts = cursor.fetchall()
        return cts
    except sqlite3.Error as e:
        print(e)
        return []


def get_students(connection, ci_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT students.first_name, students.last_name,
            countries.title, 
            cities.title, cities.area 
            FROM students 
            INNER JOIN cities ON students.city_id = cities.id 
            INNER JOIN countries ON cities.country_id = countries.id 
            WHERE cities.id = ?
            ''', (ci_id,))
        sts = cursor.fetchall()
        return sts
    except sqlite3.Error as e:
        print(e)


conn = sqlite3.connect('hw-8.db')
if conn:
    print('Connected to database.')

    cities = get_cities(conn)

    print('You can display a list of students by the selected city '
          'id from the list of cities below, to exit the program, enter 0:')
    for city in cities:
        print(f'{city[0]}. {city[1]}')

    while True:
        city_id = input('Enter the city id: ')
        if city_id == '0':
            break
        elif city_id > '7' or city_id < '0':
            print('\nThere is no city with this id. Try again.\n')
        else:
            city_id = int(city_id)
            students = get_students(conn, city_id)
            print('\nList of students in the selected city:')
            for student in students:
                print(
                    f'FULL NAME: {student[0]} {student[1]}, COUNTRY: {student[2]}, CITY: {student[3]}, CITY AREA: {student[4]}')
            print()

    conn.close()
else:
    print('Failed to connect to database.')
