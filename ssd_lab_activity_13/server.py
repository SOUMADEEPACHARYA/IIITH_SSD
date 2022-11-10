# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


import sqlite3
from flask import Flask, redirect, url_for, request

app=Flask(__name__)

@app.route('/signup',methods = ['GET'])
def signup():
    name1=input("Enter Name: ")
    email1=input("Enter email id: ")
    password1=input("Enter password: ")
    
    conn.execute("INSERT INTO data (name,email,password)  VALUES (?,?,?)",(name1,email1,password1) )
    
    print ("signup successfully", name1)
   #  redirect(url_for('succfun',name = name1))
@app.route('/signup',methods = ['GET'])
def login():
   name1=input("Enter Name: ")
   password1=input("Enter password: ")
   l=conn.execute("select password from data where name=$name1")
   if password1==l:
      print("login successfully "+name1)
   else :
      print("invalid username or password")

conn = sqlite3.connect('data.db')
print("Opened database successfully")
conn.execute('DROP TABLE  IF EXISTS data')
conn.execute('CREATE TABLE data (name TEXT, email TEXT, password TEXT)')
print ("Table created successfully")
signup()
login()

if __name__ == '__main__':
   app.run(port=8000, debug = True)
# conn.close()