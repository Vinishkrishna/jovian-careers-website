#Flask is a class
from flask import Flask, render_template,jsonify
#jsonify converts anything into json object
#render template to include the html file
#Flask object created
app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs.15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,USA',
    'salary':'$150,000'
  }
]
#/route stands for everything after domain name
#@ is used to provide some advanced functionality to the library
@app.route("/")
#jobs is like an argument provided to home.html
def hello_jovian():
  return render_template("home.html",jobs=JOBS,company_name='Jovian')
 
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  #to run the program on local device
  app.run(host='0.0.0.0', debug=True)
#before creating a website one should first make a outline of website either through tools like figma/in paper.
#anything inside static folder is available to home.html like files.