import pymongo
import uuid

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

db = myclient['sth']

collect = db['record']

# for post in collect.find():
    # print(post)

SOMETHING = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Kai',
        'comment': 'a handsome boy',
        'check': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Mi',
        'comment': 'a little girl',
        'check': False
    }
]

myquery = { "title": "Kai" }
newvalues = { "$set": { "title": "KAKA" } }

#collect.update_one(myquery, newvalues)
# collect.insert_many(SOMETHING)
# collect.drop()

cursor = collect.find()
for x in cursor:
    print(x.get('title'))
