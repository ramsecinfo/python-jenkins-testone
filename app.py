from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return "<center><h1>Welcome to Jenkins CI/CD Pipeline for Python Application<h1/><center>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')