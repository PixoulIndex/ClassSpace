import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Add to documents
data = {'name': 'Kenny'}
#db.collection('persons').add(data) #use this to auto generate ID
#db.collection('persons').document("Kenny's").set(data) #set ID

#Read file/documents with known ID
# result = db.collection('persons').document("Kenny's").get()
# if result.exists:
#     print(result.to_dict())

#get all document in the collection
docs = db.collection('persons').get()
for doc in docs:
    print(doc.to_dict())