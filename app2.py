# from flask import Flask 
# from flask_mysqldb import MySQL 

# app = Flask(__name__)

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '12345'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DB'] = 'meter'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mysql = MySQL(app)

# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     #cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')

#     #cur.execute('''INSERT INTO example VALUES (1, 'Anthony')''')
#     #cur.execute('''INSERT INTO example VALUES (2, 'Billy')''')
#     #mysql.connection.commit()

#     cur.execute('''SELECT * FROM meters''')
#     results = cur.fetchall()
#     print(results)
#     return str(results[1]['id'])

# #run flask app
# if __name__ == "__main__":
#     app.run(debug=True,host ="localhost",port=5000)

class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")
print(stu1.firstname)

pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
   pass
   if (p == 0):
       current = p
       break
   elif (p % 2 == 0):
       continue
   print(p)    # output => 1 3 1 3 1
print(current)