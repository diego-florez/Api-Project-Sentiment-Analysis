import os
import dotenv
dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")
help = "https://github.com/diego-florez/Api-Project-Sentiment-Analysis"