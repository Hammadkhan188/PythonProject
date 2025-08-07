import firebase_admin
from firebase_admin import credentials,firestore

creden=credentials.Certificate("C:\\Users\\asp\\PycharmProjects\\PythonProject\\result.json")
firebase_admin.initialize_app(creden)

db=firestore.client()

print("Connection with Firebase - Firestore")

name=input("Please Enter Name")
fname=input("Please Enter father Name")
phon=input("Please Enter phone")
addre=input("Please Enter address")
english=int(input("Please Enter english marks"))
urdu=int(input("Please urdu marks"))
math=int(input("Please math marks"))

total=english+urdu+math
percent=(total/300)*100

fetch_result=db.collection("result").document()
fetch_result.set({
    "Name" : name,
    "Fname" : fname,
    "Phone" : phon,
    "Address": addre,
    "Englishmarks" : english,
    "Urdumarks" :urdu,
    "Mathmarks" : math,
    "Total" :total,
    "Percentage" :percent

})

print("Student Record added Successfully")