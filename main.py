import requests
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      print(user)
      return user
   else:
      return render_template('hello.html')
    
if __name__ == '__main__':
   app.run()