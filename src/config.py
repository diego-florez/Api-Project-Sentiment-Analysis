from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

#Local Connection
PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")

#API Documentation
help = "https://github.com/diego-florez/Api-Project-Sentiment-Analysis"

#MongoDB
id = os.getenv("id")
myclient = MongoClient(f"mongodb://localhost:{id}/")
db = myclient["chat"]