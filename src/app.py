
from flask import Flask, request
from src.config import *
from src.mongo import *

app = Flask(__name__)


@app.route("/")
def baseResponse():
    return {
        "Hi! Welcome to the cartoon App": f"We will be guiding you through the whole process. 1st use the following command to add your user: /user/add. However, if you have any doubts during the procress, you can find all the info of how to use it here --> {help} "
        }



@app.route("/user/add", methods=["POST"])
def userAdd():
    new_chat = {"chatId":0, "chat":request.form.get("chat_name"), "userId":0, "name":request.form.get("name"), "textId":0, "text":request.form.get("text")}
    mongo_nchat = m_UserAdd(new_chat)
    return {
        "Congrats! You have been added to the cartoon App": "However your chat is empty, so do you wanna know new friends? Please use the following command: user/your-name/recommend"
        }
