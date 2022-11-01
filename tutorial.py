from pyArango.connection import *

conn = Connection(username="root", password="12345")

db = conn["mydev"]

devCollection = db.createCollection(name="mydevCollection")
print(db)
print(db["mydevCollection"])
