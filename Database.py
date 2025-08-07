import mysql.connector

con= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)
db_info =con.cursor()

print("Introduction of Person")
name=input("Enter Your Name")
fname=input("Enter Your Father Name")
phone=input("Enter Your Father Phone")
address=input("Enter Your Address")

query ="INSERT INTO `subhan`(`Name`, `Father_Name`, `Father_Phone`, `Address`) VALUES (%s,%s,%s,%s)"
value=(name,fname,phone,address)

run=db_info.execute(query,value)
con.commit()

print(f"{name} data has been saved Successfully")

con.close()
