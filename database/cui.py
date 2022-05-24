import pandas as pd
dataset=pd.read_csv('database/timetable.csv')
print(dataset.loc[:3])
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
# #   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
