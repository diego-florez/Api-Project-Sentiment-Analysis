
from flask import Flask, request
from src.config import *
from src.mongo import *
from src.nlp import getSentiment

app = Flask(__name__)


@app.route("/")
def baseResponse():
    return {
        "Hi! Welcome to the cartoon App": f"We will be guiding you through the whole process. 1st use the following command to add your user and create a chat: /user/add. However, if you have any doubts during the procress, you can find all the info of how to use it here --> {help} "
        }


@app.route("/user/add", methods=["POST"])
def userAdd():
    new_chat = {"chatId":0, "chat":request.form.get("chat_name"), "userId":0, "name":request.form.get("name"), "textId":0, "text":request.form.get("text")}
    mongo_chat = m_UserAdd(new_chat)
    return {"Congrats! You have been added to the cartoon App": "However your chat is empty, so you wanna know new friends? Please use the following command: user/<name>/<chat_name>/recommend"}


@app.route("/user/<name>/<chat_name>/recommend", methods=["GET"])
def recommend(name, chat_name):
    user, coll = name, chat_name
    df = findUser(user, coll)
    result = getRecommend(extractColls,df)
    return {"Here you have the your most similar users and their similarity with you!": result.to_dict("index")
    , "They are cool right?": "Now you can use again the command user/add again to create a chat with your friends",
    "By the way":"If you want to analyze the sentiment of your new friends use the command /user/<phrase>/get_sentiment"}
    

@app.route("/user/<phrase>/get_sentiment", methods=["GET"])
def sentiment(phrase):
    return getSentiment(phrase)