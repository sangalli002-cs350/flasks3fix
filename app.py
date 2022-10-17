import boto3
s3_resource = boto3.resource('s3')

from flask import Flask
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Jim!"

  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)


if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)

