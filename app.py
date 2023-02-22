#Flask is a class
from flask import Flask, render_template
#render template to include the html file
#Flask object created
app = Flask(__name__)


#route stands for everything after domain name
#@ is used to provide some advanced functionality to the library
@app.route("/")
def hello_world():
  return render_template("home.html")


if __name__ == '__main__':
  #to run the program on local device
  app.run(host='0.0.0.0', debug=True)
#before creating a website one should first make a outline of website either through tools like figma/in paper.
#anything inside static folder is available to home.html like files.