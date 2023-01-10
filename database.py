import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1930"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Disney")