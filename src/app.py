
from flask import Flask, request
from src.config import *

app = Flask(__name__)


@app.route("/base")
def baseResponse():
    return {
        "Hi! Welcome to the cartoon API": f"For info of how to use it refer to --> {help} "
        }



@app.route("/user/add", methods=["POST"])
def userAdd():
    saludo = request.form.get("user")
    return "ok"
