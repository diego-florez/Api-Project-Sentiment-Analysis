# Api-Project-Sentiment-Analysis

# 1 Intro:
In this repository you will find a project about NLP, MongoDB and how to deploy an App in Heroku using Docker. In this case, we will create and app, where you can add users, chats and text. Also you can find the 6 Simpson and South Park charts that are more similar to you, based in the text you introduce and you can get the sentiment of any text. Finally the app will be deployed in Heroku.

# 2 Goals:
The main goal of this project is to create an app which allows you to add users, chats and comments, and also recommend users and get their sentiment. Also, the second goal is to deploy it in Heroku.

# 3 Steps:
To fulfil the previous goals the next steps have been done:

INPUT (2 datasets downloaded from Kaggle and cleaned to sent to mongoDB as dict)
src (get user posts with flask, add info to mongoDB, use NLP techniques to recommend users and get sentiment analysis)
calls.ipynb (jupyter notebook to debug our app)
api.py (the main file)


# 4 Final Output:
The final output is an Heroku app, where you can add user, chats and comments. Also you can find similar Simpson and South Park chars based in your commends, and finally get the sentiment of any text.

# Additional Info:
1. Source: we have taken 2 datasets from Kaggel with chars and comments from the Simpson and South Park series.
2. Conditions:
- We use Docker to deploy the app in Heroku

# How does it work?
1. Go to --> http://cartoon-api.herokuapp.com
2. Add users, chats and comments with the command --> /user/{name}/{chat_name}/{text}/create
3. Get recommendations of new friends based in the text you added --> /user/{name}/{chat_name}/recommend
4. Now create another chat with the users you like --> /user/{name}/{chat_name}/{text}/create
5. You can also get the sentiment of any text --> /user/{phrase}/get_sentiment
