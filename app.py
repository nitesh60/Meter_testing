from flask import Flask, render_template, flash, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import time
import json
#create the object of Flask
app  = Flask(__name__)

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/meter'

db = SQLAlchemy(app)
 
 
#our model
class meters(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(1000), unique = True)
 
    def __init__(self, id, label):
        self.id = id
        self.label = label

class meter_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    meter_id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.DateTime, primary_key = True)
 
    def __init__(self, id, meter_id,timestamp):
        self.id = id
        self.meter_id = meter_id
        self.timestamp = timestamp
        self.value = value
obj = {}
obj_arr = []
obj1 = {}
obj1_arr = []
students = meters.query.all()
for i in students:
    obj = {"id": i.id, "label" : i.label}
    obj_arr.append(obj)
students1 = meter_data.query.all()
for j in students1:
    obj1 = {"id": j.id, "meter_id": j.meter_id, "timestamp": str(j.timestamp), "value": j.value}
    obj1_arr.append(obj1)
#creating our routes
@app.route('/meters/',methods=['GET', 'POST'])
def index():
    obj = {}
    obj_arr = []
    obj1 = {}
    obj1_arr = []
    students = meters.query.all()
    for i in students:
        obj = {"id": i.id, "label" : i.label}
        obj_arr.append(obj)
    students1 = meter_data.query.all()
    for j in students1:
        obj1 = {"id": j.id, "meter_id": j.meter_id, "timestamp": j.timestamp, "value": j.value}
        obj1_arr.append(obj1)

    return render_template('index.html',data = obj_arr,data1=students1)

@app.route('/meters/x/url/detail',methods=['GET', 'POST'])
def index1():
    id = request.args.get('id')
    obj1 = {}
    obj1_arr = []
    final_value = []
    students1 = meter_data.query.all()
    for j in students1:
        obj1 = {"id": j.id, "meter_id": j.meter_id, "timestamp": j.timestamp, "value": j.value}
        obj1_arr.append(obj1)
    return render_template('index1.html',id=int(id),json_file = obj1_arr)

#login route
@app.route('/meters/<id>' , methods = ['GET', 'POST'])
def data_show_page(id):
    # print(id)
    search_arr = []
    obj1_arr.sort(key=lambda x:time.mktime(time.strptime(str(x['timestamp']), '%Y-%m-%d %H:%M:%S')))
    print(type(obj1_arr))
    final = json.dumps(obj1_arr, indent=2)
    print(type(json.loads(final)))
    for i in obj1_arr:
        print(type(i['meter_id']))
        if i['meter_id'] == int(id):
            search_arr.append(i)
    print(search_arr)
    
    return render_template('search.html',jsonobj = json.loads(final),search = search_arr)

#run flask app
if __name__ == "__main__":
    app.run(debug=True,host ="localhost",port=5000)