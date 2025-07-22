# ResturentName =" KababJees Burger"
# Address=" Defence Phase 8"
# Speciality="Fast Food"
# Phone="03132677651"
# CityName="Karachi"
# Is_FiveStart=True
#
# print(f"Name is{ResturentName} \n Address is{Address} \n SpecialFood is{Speciality} \n Phone is{Phone} \n City is{CityName} \n FiveStar is{Is_FiveStart}")

# ResturentName =input("Enter Your Resturent Name:")
# Address=input("Enter Your Address:")
# Speciality=input("Enter The Speciality:")
# Phone=int(input("Enter Your Number:"))
# CityName=input("Enter Your City:")
# Is_FiveStart=bool(input("FiveStar Rating:"))

# print("Dholo bholo halwa puri shop")
# Poris=int(input("How Many Puries do you want ?"))
# Chole=int(input("How Many Chole plate do you want ?"))
# Aloo=int(input("How Many aloo plate do you want ?"))
# Halwa=int(input("How Many halwa plate do you want ?"))
# perpuri=50
# choleplate=100
# aloo=80
# halwa=150
# puriTotal=perpuri*Poris
# choletotal=choleplate*Chole
# aloototal=aloo*Aloo
# halwatotal=halwa*Halwa
# total=puriTotal+choletotal+aloototal+halwatotal
# tax=total*0.16
# finaltotal=total+tax
# discount=finaltotal*0.5
# billafterdisc=finaltotal-discount
#
# print(f"Your bill is {total} \n your tax is {tax} \n Final Total {finaltotal} \n discount is{discount} \n bill after discount{billafterdisc}")


name=input("Enter your Name")
salery=float(input("Enter your salery"))

print("expense Calculator")
groccerybill=float(input("Enter your Groccesrybill"))
kebill=float(input("Enter your Ke bill"))
gasbill=float(input("Enter your Gasbill"))
internetbill=float(input("Enter your internetbill"))
waterbill=float(input("Enter your waterbill"))
jamadarybill=float(input("Enter your jamadarbill"))
supercardbill=float(input("Enter your supercardbill"))
transportbill=float(input("Enter your transportbill"))
ownhouse=input("In your own house")

if ownhouse.lower()=="no":
    rent = float(input("Enter your rent"))

else:
    rent=0

married=input("are you married")
if married.lower()=="yes":
    child = int(input("how many childerten do you have"))
    if child>0:
        childexpense=float(input("enter your child expense"))
    else:
        childexpense=0

totalexpens=groccerybill+kebill+gasbill+internetbill+waterbill+jamadarybill+supercardbill+transportbill+rent+childexpense

saving=salery-totalexpens
if salery>totalexpens:
    print(f"{name} saving are {saving}kindly visit meezan bank")
elif salery==totalexpens:
    print("you should increase your salery")
else:
    print("decrease your expense")

print(f"your salery is{salery} \n your total expens is {totalexpens} \n yor saving is{saving}")
