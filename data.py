# -*- coding: utf-8 -*-
import sqlite3
from os.path import dirname, realpath


main_path = dirname(realpath(__name__))

conn = sqlite3.connect(main_path + '/data/cars.db')
cursor = conn.cursor()
 
# Создание таблицы
'''
cursor.execute("""CREATE TABLE name
                  (id integer primary key, firm text, model text, 
                   engine_type text, engine_volume integer, 
                   engine_power integer, engine_moment integer, 
                   engine_fuel_consumption_dealer float, 
                   engine_fuel_consumption_user float, 
                   engine_fuel_consumption_avg float, price integer, 
                   user_defined_expense integer, to_0_length integer,
                   to_0_price, to_1_length integer, to_1_price, 
                   to_2_length integer, to_2_price, 
                   to_3_length integer, to_3_price, 
                   to_4_length integer, to_4_price, 
                   to_5_length integer, to_5_price, 
                   transport_tax integer)
               """)
'''

def add_changings(model, field, value):
    pass

def new_car():
    pass


'''
cursor.execute("""CREATE TABLE options
                  (id integer primary key, model text, 
                  
                  )
               """)
'''

# Написать readme.txt