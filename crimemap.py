from dbhelper import DBHelper
from flask import Flask,render_template,request
import json
import dateparser
import datetime
import string

import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


categories = ['mugging','break-in']


app = Flask(__name__)
DB = DBHelper()

@app.route('/')
def home(erro_message=None):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes,categories=categories,error_message=error_message)



@app.route('/submitcrime', methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in categories:
	return home()
    
    date = request.form.get("date")
    if not date:
	return home("Inavlid date. Please use yyyy-mm-dd format")
    try:
	longitude = float(request.form.get("longitude"))
    	latitude = float(request.form.get("latitude"))
    except ValueError:
	return home()
    description = request.form.get("description")
    description = sanitize_string(request.form.get("description"))
    DB.add_crime(category, date, latitude, longitude, description)
    return home()



def sanitize_string(userinput):
	whitelist = string.letters + string.digits + " !?$.,;:-'()&"
	return filter(lambda x: x in whitelist, userinput)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
