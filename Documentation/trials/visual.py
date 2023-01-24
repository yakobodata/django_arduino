import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import Error
import datetime
import time
from time import sleep
from time import time, ctime
from time import gmtime, strftime
from datetime import timedelta

# To Calculate the hours of a specific date 
# I need to get the info from the database 
# They have turned out to be tuples

#i will use those hours my x axis

try:
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="gametracking")
    #Get current date
    x = datetime.datetime.now()

    currentdate = x.strftime("%x")

    print(currentdate)
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Track WHERE date = '%s' " % (currentdate))

    myresult = mycursor.fetchall()

    sql_data = pd.DataFrame(myresult)

    #sql_data.to_excel("gametracking.xlsx", sheet_name="GameTrack", index=False)

    mydb.close()

    # print(sql_data)

    #rename columns
    rename_motion = sql_data.columns = ['id', 'status', 'date', 'time']
   
    #am interested in only motion moved

    sql_data.to_excel("gametracking.xlsx", sheet_name="GameTrack", index=True)

    print(sql_data)

    #change status into numeric
    convert_dict = {'status': int } 
  
    sql_data = sql_data.astype(convert_dict) 
    print(sql_data.dtypes) 

    print("InitalTime")
    print(sql_data["time"].min())
    print("EndTime")
    print(sql_data["time"].max())

    print("TimeDifference")
    print(sql_data["time"].max()-sql_data["time"].min())

    #plot
    x_axis = sql_data["time"].values
    y_axis = sql_data["status"].values

    # plot dataframe
    
    plt.plot(x_axis,y_axis)
    plt.xlabel('time')
    plt.ylabel('status')
    plt.show()

except Error as e:
    print("Error while connecting to MySQL", e)





