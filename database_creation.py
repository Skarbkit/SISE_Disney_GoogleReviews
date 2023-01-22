import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host="localhost",
  database='disney',
  user="root",
  password="1930"
)

#mycursor = mydb.cursor()
if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]



if "structure" in tables:
  print("structure already exists")
else:
  table = ('''CREATE TABLE structure (
      ID int primary key NOT NULL,
      type varchar(255),
      name varchar(255)
  );''')
  cursor.execute(table)
  print('Table created: structure')


if "sitereview" in tables:
  print("sitereview already exists")
else:
  table = ('''CREATE TABLE sitereview (
      ReviewID int primary key NOT NULL AUTO_INCREMENT,
      Name varchar(255),
      ReviewRate int,
      ReviewTime varchar(255),
      RewiewVisite varchar(255),
      ReviewText text,
      SiteType int,
      FOREIGN KEY (SiteType) REFERENCES structure(ID)
  );''')
  cursor.execute(table)
  print('Table created: sitereview')

if "hostelreview" in tables:
  print("hostelreview already exists")
else:
  table = ('''CREATE TABLE hostelreview (
      hostelID int primary key NOT NULL AUTO_INCREMENT,
      Name varchar(255),
      ReviewRate int,
      ReviewTime varchar(255),
      ReviewVisite varchar(255),
      ReviewText text,
      VoyageType varchar(255),
      RoomRate double,
      EmplacementRate double,
      ServiceRate double,
      HostelType int,
      FOREIGN KEY (HostelType) REFERENCES structure(ID)
  );''')
  cursor.execute(table)
  print('Table created: hostelreview')

