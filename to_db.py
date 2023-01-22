import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

os.chdir('datasets/')


mydb = mysql.connector.connect(
  host="localhost",
  database='disney',
  user="root",
  password="1930"
)

# create cursor
cursor=mydb.cursor()

cursor.execute('''INSERT INTO structure (ID,type,name) values 
(21,'hotel','Crockett Ranch'),
(22,'hotel','Cheyenne'),
(23,'hotel','Santa Fe'),
(24,'hotel','Newport Bay Club'),
(25,'hotel','Sequoia Lodge'),
(26,'hotel','New York - The Art of Marvel')
''')

mydb.commit()


dict = {1:'Disney_s Davy Crockett Ranch 14h33-22-01.csv',2:'Disney_s Hotel Cheyenne 10h57-22-01.csv',3:'Disney_s Hotel Santa Fe 13h42-22-01.csv',4:'Disney_s Newport Bay Club 00h26-22-01.csv',5:'Disney_s Sequoia Lodge 10h24-22-01.csv',6:"Disney's Hotel New York - The Art of Marvel 20h59-21-01.csv"}

for l in range(1,len(dict)+1):
  data = pd.read_csv(dict[l])

  data.columns=['Name','ReviewRate','ReviewTime','ReviewVisite','ReviewText','VoyageType','RoomRate','EmplacementRate','ServiceRate']
  data['HostelType']=20+l


  cols = ",".join([str(i) for i in data.columns.tolist()])

  print(data['HostelType'][0])

  data = data.fillna("Null")
  for i,row in data.iterrows():
      sql = "INSERT INTO `hostelreview` (" + cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"

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

