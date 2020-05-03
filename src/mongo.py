from src.config import *
from src.nlp import getCosineSim
import pandas as pd


def m_UserAdd(new_chat):
    mycol = db[new_chat["chat"]]
    colls = len(db.list_collection_names())
    docs = (mycol.find().count())
    new_chat["userId"] = docs 
    new_chat["textId"] = docs
    new_chat["chatId"] = colls-1 if docs>0 else colls
    return mycol.insert_one(new_chat)

def extractColls():
    simpson = list(db["simpson"].find({},{"_id":0,"name":1,"text":1}).limit(1000))
    simpson_df = pd.DataFrame(simpson)
    south_park = list(db["south_park"].find({},{"_id":0,"name":1,"text":1}).limit(1000))
    south_park_df = pd.DataFrame(south_park)
    df_joint = pd.concat([simpson_df,south_park_df])
    return df_joint


def findUser(user, coll):
    data = list(db[coll].find({"name":user},{"_id":0,"name":1,"text":1}))
    df = pd.DataFrame(data)
    return df

def getRecommend(extractColls,df):
    df = pd.concat([df,extractColls()])
    users = list(df.name)
    phrases = list(df.text)
    rels = getCosineSim(phrases)

    rels_df_users = pd.DataFrame(rels,columns=users,index=users)

    rels_df_phrases = pd.DataFrame(rels,columns=phrases,index=phrases)

    top_users = rels_df_users.iloc[:,0].sort_values(ascending=False)[1:7]

    top_phrases = rels_df_phrases.iloc[:,0].sort_values(ascending=False)[1:7]

    result_users = top_users.to_frame().reset_index().rename(columns={"index":"User",top_users.name:"Similarity"})

    result_phrases = top_phrases.to_frame().reset_index().rename(columns={"index":"Phrase",top_phrases.name:"Similarity"})

    mergedDf = result_users.merge(result_phrases, on='Similarity')

    return mergedDf


