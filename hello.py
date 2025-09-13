from flask import Flask

app = Flask(__name__)

@app.route('/') #this is the index file
def hello():
    return 'Hello, World!'