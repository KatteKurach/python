from .models import User, Airplane, Airport, Timetable, History
from  django.db import connection
import sqlite3

#_____________TABLE USER______________________

def add_user(name, user_email, user_password):
    sql_check = "SELECT * FROM timetable_user WHERE email = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_check, (user_email,))
    if (len(cursor.fetchall()) == 0) :
        sql_string = "INSERT INTO timetable_user (user_name, email, password, access_level) \
                                                VALUES (?,?,?,?)"
        cursor.execute(sql_string, (name, user_email, user_password, 0))
    conn.commit()
    conn.close()

def remove_user(email):
    sql_str = "DELETE FROM timetable_user WHERE email = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str, (email,))
    conn.commit()
    conn.close()

def get_list_users():
    sql_str = "SELECT * FROM timetable_user"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str)
    temp = cursor.fetchall()
    conn.commit()
    conn.close()
    return temp

def check_user(email, password):
    sql_str = "SELECT * FROM timetable_user WHERE email = ? and password = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str, (email, password))
    if (len(cursor.fetchall()) == 0):
        isIn = False
    else:
        isIn = True
    conn.commit()
    conn.close()
    return isIn


#_____________TABLE AIRPLANE________________

def add_airplane(cost, seats, free_seats):
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    sql_string = "INSERT INTO timetable_airplane (cost, seats, free_seats) \
                                                VALUES (?,?,?)"
    cursor.execute(sql_string, (cost, seats, free_seats))
    conn.commit()
    conn.close()

def remove_plane(cost, seats, free_seats):
    sql_str = "DELETE FROM timetable_airplane WHERE cost = ? and seats = ? and free_seats = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str, (cost, seats, free_seats))
    conn.commit()
    conn.close()


def get_list_airplanes():
    sql_str = "SELECT * FROM timetable_airplane"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str)
    temp = cursor.fetchall()
    conn.commit()
    conn.close()
    return temp

#_____________TABLE AIRPORT_____________

def add_airport(airport_name, country):
    sql_check = "SELECT * FROM timetable_airport WHERE airport_name = ? and country = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_check, (airport_name, country))
    if (len(cursor.fetchall()) == 0) :
        sql_string = "INSERT INTO timetable_airport (airport_name, country) \
                                                VALUES (?,?)"
        cursor.execute(sql_string, (airport_name, country))
    conn.commit()
    conn.close()


def remove_airport(airport_name, country):
    sql_str = "DELETE FROM timetable_airport WHERE airport_name = ? and country = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str, (airport_name, country))
    conn.commit()
    conn.close()


#_____________TABLE TIMETABLE______________

def add_timetable(plane, dep_time, arr_time, place_from, place_to, dep_date, arr_date):
    sql_check = "SELECT * FROM timetable_timetable WHERE plane = ? and departure_time = ? and arrival_time = ? \
                    departure_date = ? and arrival_date = ? and place_from = ? and place_to = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_check, (plane, dep_time, arr_time, dep_date, arr_date, place_from, place_to))
    if (len(cursor.fetchall()) == 0) :
        sql_string = "INSERT INTO timetable_timetable (plane, departure_time, arrivale_time, departure_date,  \
                      arrival_date, place_from, place_to) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(sql_string, (plane, dep_time, arr_time, dep_date, arr_date, place_from, place_to))
    conn.commit()
    conn.close()

def remove_timetable(plane, dep_time, arr_time, place_from, place_to, dep_date, arr_date):
    sql_str = "DELETE FROM timetable_user WHERE  plane = ? and departure_time = ? and arrival_time = ? \
                    departure_date = ? and arrival_date = ? and place_from = ? and place_to = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_str, (plane, dep_time, arr_time, dep_date, arr_date, place_from, place_to))
    conn.commit()
    conn.close()


#_____________TABLE HISTORY______________

def add_history(user, flight):
    sql_check = "SELECT * FROM timetable_history WHERE user = ? and flight = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor = conn.cursor()
    cursor = conn.execute(sql_check, (user, flight))
    if (len(cursor.fetchall()) == 0) :
        sql_string = "INSERT INTO timetable_history (user, flight) \
                                                VALUES (?,?)"
        cursor.execute(sql_string, (user, flight))
    conn.commit()
    conn.close()

def get_list_history(email):
    sql_get_user = "SELECT * FROM timetable_user WHERE email = ?"
    sql_str = "SELECT * FROM timetable_history WHERE user = ?"
    conn = sqlite3.connect('/Users/ekaterinakurach/python/skylines/db.sqlite3')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor2 = conn.execute(sql_get_user, (email,))
    cursor1 = conn.execute(sql_str, (cursor2,))
    temp = cursor1.fetchall()
    conn.commit()
    conn.close()
    return temp


