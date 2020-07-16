import pymongo
import uuid

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['sth']
collect = db['record']

# for post in collect.find():
    # print(post)

def insertMany(SOMETHING=None):
    collect.insert_many(SOMETHING)
    return 'DOWN'

def clear():
    collect.drop()
    return 'DOWN'

def updateOne(myquery, newvalues):
    print(myquery, newvalues)
    collect.update_one(myquery, newvalues)
    return 'DOWN'

def queryAll(getWhat=None):
    cursor = collect.find()
    for x in cursor:
        # print(x.get('title'))
        print(x)
    return 'DOWN'




