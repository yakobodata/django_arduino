import mysql.connector
from mysql.connector import Error
import datetime
import serial
import time
from time import time
from time import sleep
from time import time, ctime
from time import gmtime, strftime
from stopwatch import Stopwatch
from timeit import default_timer as timer
from datetime import timedelta
import pandas as pd



try:
    connection = mysql.connector.connect(host='localhost',database='gametracking',user='root',
                                        password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

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
                # Now, let's decode/convert them into a string
                s = data.decode('UTF-8')
                print(s)
                motion_time = 0.0 
                stopwatch = Stopwatch() # Stopwatch keeps running

                if s == "1": 
                    #Get current time
                    x = datetime.datetime.now()
                    currenttime = x.strftime("%X")
                    # print("Inactive_time")
                    print(currenttime)
                    #get this current time put it somewhere
                    # stopwatch.start() # Start it again
                    # stopwatch.restart() # reset and start again
                    # t = time.process_time()
                    start = timer()
                else:
                    #Get current time
                    c = datetime.datetime.now()
                    currenttime = c.strftime("%X")
                    # print("Inactive_time")
                    print(currenttime)
                    #do some stuff
                    # elapsed_time = time.process_time() - t
                    # print("active_time")
                    # print(elapsed_time)
                    end = timer()
                    print("Been Active for")
                    motion_bit = timedelta(seconds=end-start)
                    print(motion_bit)
                    #put them inside an array
                    
            
                #current date
                y = datetime.datetime.now()
                currentdate = y.strftime("%x")
                print(currentdate)
               
                cursor = connection.cursor()
                # cursor.execute(mySql_insert_query)
                cursor.execute("INSERT INTO Track(status, date, time)  VALUES (%s, %s, %s)", (data, currentdate, str(currenttime)))
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into Track table")
                #cursor.close()
        print(motion_bits)
except Error as e:
    print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
        # cursor.close()
        # connection.close()
        # print("MySQL connection is closed")
