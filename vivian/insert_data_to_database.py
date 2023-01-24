import mysql.connector
from mysql.connector import Error
import datetime
import serial
import time
from time import time
from time import sleep
from time import time, ctime
from time import gmtime, strftime
#from stopwatch import Stopwatch
from timeit import default_timer as timer
from datetime import timedelta
import pandas as pd
import django
import os
import codecs
import sqlite3

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'vivian.settings')

django.setup()

from bit_game.models import Track




try:
    connection = sqlite3.connect("/home/ubuntu/.code/django_arduino/vivian/db.sqlite3")
    if connection:
        # db_Info = connection.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        # cursor = connection.cursor()
        # cursor.execute("select database();")
        # record = cursor.fetchone()
        # print("You're connected to database: ", record)

        #Arduino Startingg.......
        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
        #Arduino Data
        # t = time()
        # ti= ctime(t)
       
        while True:
            data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
            if data:
                print ( ":" ,data)
                #change data variable from bytes to String

                # setdata = data.decode('utf-8')
                # s = data[0]

                data = data.decode('utf-8')

                # print(s)
                # motion_time = 0.0 
                # stopwatch = Stopwatch() # Stopwatch keeps running

                if data == "1": 
                    #Get current time
                    x = datetime.datetime.now()
                    currenttime = x.strftime("%X")
                    # print("Inactive_time")
                    print(currenttime)
                    #get this current time put it somewhere
                    # stopwatch.start() # Start it again
                    # stopwatch.restart() # reset and start again
                    # t = time.process_time()
                    # global start
                    # start = timer()
                    y = datetime.datetime.now()
                    # currentdate = y.strftime("%x")
                    currentdate = y.strftime("%Y-%m-%d")
                    print(currentdate)
                   
                    cursor = connection.cursor()
                    
                    cursor.execute('INSERT INTO bit_game_track (status,date,time) ''VALUES (?, ?, ?)', (data, currentdate, str(currenttime)))
                    connection.commit()
                    print(cursor.rowcount, "Record inserted successfully into Track table")
                     
                elif data == "0":
                    #Get current time
                    c = datetime.datetime.now()
                    currenttime = c.strftime("%X")
                    # print("Inactive_time")
                    print(currenttime)

                    y = datetime.datetime.now()
                    # currentdate = y.strftime("%x")
                    currentdate = y.strftime("%Y-%m-%d")
                    print(currentdate)
                   
                    cursor = connection.cursor()
                   
                    cursor.execute('INSERT INTO bit_game_track (status,date,time) ''VALUES (?, ?, ?)', (data, currentdate, str(currenttime)))

                    connection.commit()
                    print(cursor.rowcount, "Record inserted successfully into Track table")
                    #do some stuff
                    # elapsed_time = time.process_time() - t
                    # print("active_time")
                    # print(elapsed_time)

                    # end = timer()
                    # print("Been Active for")
                    # motion_bit = timedelta(seconds=end - start)
                    # print(motion_bit)
                    #end = timer()
                    #print("Been Active for")
                    #motion_bit = timedelta(seconds=end-start)
                    #print(motion_bit)

                    #put them inside an array
                else:
                    continue
                    
            
                #current date
                
                #cursor.close()
        print(motion_bits)
except Error as e:
    print("Error while connecting to MySQL", e)



# finally:
#     if (connection.is_connected()):
        # cursor.close()
        # connection.close()
        # print("MySQL connection is closed")


# try:
#     connection = mysql.connector.connect(host='localhost',database='bit_game',user='jacob',
#                                         password='vivian@123')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

#         #Arduino Startingg.......
#         arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
#         #Arduino Data
#         # t = time()
#         # ti= ctime(t)
       
#         while True:
#             data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
#             if data:
#                 print ( ":" ,data)
#                 #change data variable from bytes to String

#                 # setdata = data.decode('utf-8')
#                 s = data[0]

#                 # s = data.decode('utf-8')

#                 print(s)
#                 motion_time = 0.0 
#                 stopwatch = Stopwatch() # Stopwatch keeps running

#                 if s == "1": 
#                     #Get current time
#                     x = datetime.datetime.now()
#                     currenttime = x.strftime("%X")
#                     # print("Inactive_time")
#                     print(currenttime)
#                     #get this current time put it somewhere
#                     # stopwatch.start() # Start it again
#                     # stopwatch.restart() # reset and start again
#                     # t = time.process_time()
#                     global start
#                     start = timer()
		             
#                 elif s == "0":
#                     #Get current time
#                     c = datetime.datetime.now()
#                     currenttime = c.strftime("%X")
#                     # print("Inactive_time")
#                     print(currenttime)
#                     #do some stuff
#                     # elapsed_time = time.process_time() - t
#                     # print("active_time")
#                     # print(elapsed_time)

#                     # end = timer()
#                     # print("Been Active for")
#                     # motion_bit = timedelta(seconds=end - start)
#                     # print(motion_bit)
#                     #end = timer()
#                     #print("Been Active for")
#                     #motion_bit = timedelta(seconds=end-start)
#                     #print(motion_bit)

#                     #put them inside an array
#                 else:
#                     continue
                    
            
#                 #current date
#                 y = datetime.datetime.now()
#                 # currentdate = y.strftime("%x")
#                 currentdate = y.strftime("%Y-%m-%d")
#                 print(currentdate)
               
#                 cursor = connection.cursor()
#                 # cursor.execute(mySql_insert_query)
#                 cursor.execute("INSERT INTO bit_game_track  (status, date, time)  VALUES (%s, %s, %s)", (data, currentdate, str(currenttime)))
#                 connection.commit()
#                 print(cursor.rowcount, "Record inserted successfully into Track table")
#                 #cursor.close()
#         print(motion_bits)
# except Error as e:
#     print("Error while connecting to MySQL", e)
# # finally:
# #     if (connection.is_connected()):
#         # cursor.close()
#         # connection.close()
#         # print("MySQL connection is closed")
