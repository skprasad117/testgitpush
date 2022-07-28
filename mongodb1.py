import pymongo
# pip install pymongo
client = pymongo.MongoClient("mongodb+srv://sanjay:sanjay11@cluster0.m69g2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "sanjay",
    "email" : "skprasad117@gmail.com",
    "surname" : "kumar"
}
d = {
    "name" : "sanjay",
    "email" : "skprasad117@gmail.com",
    "surname" : "kumar"
}
d = {
    "name" : "sanjay",
    "email" : "skprasad117@gmail.com",
    "surname" : "kumar"
}
d = {
    "name" : "sanjay",
    "email" : "skprasad117@gmail.com",
    "surname" : "kumar"
}

d = {
    "name" : "sanjay",
    "email" : "skprasad117@gmail.com",
    "surname" : "kumar"
}




db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)