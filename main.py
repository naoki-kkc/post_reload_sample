from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# GETでアクセスした場合に実行
@app.route('/param', methods=['GET'])
def param_get():
    return render_template('param.html', exec_method='GET')

# POSTでアクセスした場合に実行
@app.route('/param', methods=['POST'])
def param_post():
    return render_template('param.html', exec_method='POST')