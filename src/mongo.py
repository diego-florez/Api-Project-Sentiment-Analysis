from src.config import *

def m_UserAdd(new_chat):
    mycol = db[new_chat["chat"]]
    colls = len(db.list_collection_names())
    docs = (mycol.find().count())
    new_chat["userId"] = docs 
    new_chat["textId"] = docs
    new_chat["chatId"] = colls-1 if docs>0 else colls
    return mycol.insert_one(new_chat)


