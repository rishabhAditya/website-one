from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs= [
  {
    
    "id1":1,
    "title":"Data Analyst",
    "location":"Delhi",
    "salary":500000
  
  },
  {
    
    "id1":2,
    "title":"Web developer",
    "location":"Delhi"
  
  },
   {
    
    "id1":3,
    "title":"Cyber Engineer",
    "location":"WFH",
    "salary":7600000
  
  }
]

@app.route('/')
def start():
  
  return render_template('index.html',j=jobs)
@app.route('/api/jobs')
def api():
  return jsonify(jobs)
app.run(host='0.0.0.0',debug = True)
