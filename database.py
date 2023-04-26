import os
import pymysql.cursors
from flaskext.mysql import MySQL
from flask import Flask

# creates flask instance for the current python module
app = Flask(__name__)



# commands to connect to database
sql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=os.environ['PASSWORD']
app.config['MYSQL_DATABASE_DB']='railway'
app.config['MYSQL_DATABASE_PORT']=5885
app.config['MYSQL_DATABASE_HOST']=os.environ['HOST']
sql.init_app(app)
connection=sql.connect()
cursor = connection.cursor(pymysql.cursors.DictCursor)

select0_5 = 'select * from profiles'
cursor.execute(select0_5)
users_table = cursor.fetchall()

def fetch_fromId(id):
  select1 =f'select * from profiles where id={id}'
  cursor.execute(select1)
  profile_info = cursor.fetchall()
  return (profile_info)