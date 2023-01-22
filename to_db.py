import pandas as pd
import mysql.connector
from mysql.connector import Error

data = pd.read_csv(r"Disney's Hotel New York - The Art of Marvel 20h59-21-01.csv")
data.columns=['Name','ReviewRate','ReviewTime','ReviewVisite','ReviewText','VoyageType','RoomRate','EmplacementRate','ServiceRate']
data['HostelType']=21

mydb = mysql.connector.connect(
  host="localhost",
  database='disney',
  user="root",
  password="1930"
)

# create cursor
cursor=mydb.cursor()


cols = ",".join([str(i) for i in data.columns.tolist()])

for i,row in data.iterrows():
    sql = "INSERT INTO `hostelreview` (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"

    t = list()
    for i in range(len(row)):
      if row[i] == "Null":
        t.append(None)
      else:
        t.append(row[i])  

    cursor.execute(sql, tuple(t))
    # the connection is not autocommitted by default, so we must commit to save our changes
    mydb.commit()

# Confirm data import
print("Data imported to the 'hostelreview' table.")
