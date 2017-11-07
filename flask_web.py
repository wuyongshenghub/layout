#encoding:utf-8
"""
@project = python_training
@file = flask_web
@author = __Mark__
@qq = 395424820
@mail = "mark5279@163.com"
@create_time = 2017/11/7 15:11
"""

from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/user')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/hard')
def hardware():
    return render_template('hardware.html')

@app.route('/cpu')
def cpu():
    return render_template('cpu.html')

@app.route('/memory')
def memory():
    return render_template('mem.html')

@app.route('/network')
def network():
    return render_template('/network.html')


@app.route('/newadduser')
def newadduser():
    return render_template('newadduser.html')

@app.route('/set')
def set():
    return render_template('set.html')



if __name__=='__main__':
    app.run(debug=True,port=9092)