<<<<<<< Updated upstream
print("Success")


a = "test1"
=======
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


>>>>>>> Stashed changes
