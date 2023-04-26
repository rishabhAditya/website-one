from flask import Flask, render_template, jsonify, request
from database import users_table,fetch_fromId
app = Flask(__name__)

# jobs= [
#   {
    
#     "id1":1,
#     "title":"Data Analyst",
#     "location":"Delhi",
#     "salary":500000
  
#   },
#   {
    
#     "id1":2,
#     "title":"Web developer",
#     "location":"Delhi"
  
#   },
#    {
    
#     "id1":3,
#     "title":"Cyber Engineer",
#     "location":"WFH",
#     "salary":7600000
  
#   }
# ]
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
  print(data)
  return data
  
  
  
if __name__=='__main__':
  app.run(host='0.0.0.0',debug = True)
