from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

#Local Connection
PORT = os.getenv("PORT")
MGURL = os.getenv("MGURL")

#API Documentation
help = "https://github.com/diego-florez/Api-Project-Sentiment-Analysis"

#MongoDB
MGURL = os.getenv("MGURL")
myclient = MongoClient(f"{MGURL}")
db = myclient["chat"]