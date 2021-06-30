from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_openshift ():
    return 'Python + Flask - Test application to run on openshift'

app.run(host='0.0.0.0', port =8080)