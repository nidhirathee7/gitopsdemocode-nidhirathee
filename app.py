from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! from Nidhi Rathee !!!!! Welcome to GitOps World !!!!"
