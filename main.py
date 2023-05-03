from flask import Flask, render_template, jsonify, request
from database import users_table,fetch_fromId,insert_data,show_info
app = Flask(__name__)


jobs= users_table
@app.route('/')
def start():
  
  return render_template('index.html',j=jobs)
@app.route('/api/jobs')
def api():
  
  return jsonify(jobs)

@app.route('/jobs/<id>')
def id_job(id):
  profile_data=fetch_fromId(id)
  return render_template('info.html',j=profile_data[0])#jsonify(profile_data[0])

@app.route('/jobs/<id>/submit', methods=['post'])
def sub(id):
  data = request.form
  insert_data(id,data['full_name'],data['email'],data['linkedin_url'],0)
  res = 'Your application has been submitted<br>'
  res+= '<a href="/">Home</a><br>'

  return res
  
@app.route('/jobs/check')
def check():
  response = '<h3>Application Status</h3><br><br>'
  response += '<form action=/jobs/show method=post>'
  response += 'Enter email <input type=text name=useremail required><br>'
  response += '<br><br><input type=submit value=Save />'
  response += '</form>'
  return response
@app.route('/jobs/show', methods=['post'])
def show():
  data = request.form
  e = data['useremail']
  data=show_info(e)
  print(data)
  response=""
  for jobs in data:
    response+= f'Application id={jobs["user_id"]} <br>'
    response+= f'{jobs["title"]} : {jobs["company"]} <br>'
    if jobs['app_status']<0:
      response+= 'Your application has been rejected.'
    elif jobs['app_status']==0:
      response+= 'Your application will be processed shortly.'
    elif jobs['app_status']==1:
      response+= 'Your application has been selected. Recruitors will reach you. <br><br>'
    
  
 
  response+= '<br><a href="/">Home</a><br>'
  return response
  
if __name__=='__main__':
  app.run(host='0.0.0.0',debug = True)
