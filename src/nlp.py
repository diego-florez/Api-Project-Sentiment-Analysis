from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
#nltk.download('stopwords')
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()


class LemmaTokenizer:
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

tvect = TfidfVectorizer(
    #stop_words='english',
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    tokenizer=LemmaTokenizer(),
    token_pattern=r'\w{2,}',  #vectorize 2-character words or more
    ngram_range=(1, 1))

def getVectors(strs):
    text = [t for t in strs]
    vectorizer = tvect.fit_transform(text)
    return vectorizer.toarray()

def getCosineSim(strs): 
    vectors = [v for v in getVectors(strs)]
    return (cosine_similarity(vectors))


def getSentiment(text):
    return sia.polarity_scores(text) 

