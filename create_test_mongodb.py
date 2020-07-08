import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
db = myclient['sth']
 
collect = db['record']

# for post in collect.find():
    # print(post)

SOMETHING = [
    {
        'title': 'Kai',
        'comment': 'a handsome boy',
        'check': True
    },
    {
        'title': 'Mi',
        'comment': 'a little girl',
        'check': False
    }
]



# collect.insert_many(SOMETHING)

cursor = collect.find()
for x in cursor:
    print(x.get('title'))
