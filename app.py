from flask import Flask, request
from datetime import datetime
import sqlite3

from os import mkdir

try:
    conn = sqlite3.connect('sqlitedb/metrics.db')
except sqlite3.OperationalError:
    mkdir('sqlitedb')
finally:
    conn = sqlite3.connect('sqlitedb/metrics.db')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rootDir():
   if request.method == 'POST':
      dbLocation = 'sqlitedb/metrics.db'
      print(dbLocation)
      with sqlite3.connect(dbLocation) as conn:
         dt=str(datetime.now())
         data=str(request.data)
         insertQuery = """INSERT INTO POSTEDMETRICS VALUES (?, ?);"""
         cursor = conn.cursor()
         cursor.execute("""CREATE TABLE if NOT EXISTS POSTEDMETRICS (
                        timeRecorded TIMESTAMP,
                        received TEXT);""")
         cursor.execute(insertQuery, (dt, data))
         conn.commit()
         return 'Python Webapp over SSL: POST OK!\n{}\n'.format(data)   

   elif request.method == 'GET':
      return 'Python Webapp over SSL: GET OK!\n'

if __name__ == '__main__':
   app.run(host="0.0.0.0")
