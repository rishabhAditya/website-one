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

def insert_data(id,fullname,email,linkedin,app_status):
  insert1 = 'insert into users(id,fullname,email,linkedin,app_status) values(%s,%s,%s,%s,%s)'
  cursor.execute(insert1,(id,fullname,email,linkedin,app_status))
  connection.commit()

def show_info(email):
  #select1 ='select * from users where email=%s'
  select1 ='select profiles.title, profiles.company, users.user_id, users.app_status from profiles join users on profiles.id = users.id where users.email=%s'
  cursor.execute(select1,(email,))
  profile_info = cursor.fetchall()
  return (profile_info)