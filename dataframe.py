import pandas as pia
import lxml

# rishta = {
#     "name" :["subhan","anam","kinza","ali","rehman"],
#     "gender":["m","f","f","m","m"],
#     "Prefered_caste" : ["sheikh","sheikh","khan","abbasi","swati"],
#     "preferred_area" : ["dha","orangi","nazimabad","korangi","baldia"],
#     "profession" : ["software engineer","teacher","tuition","office","company"],
#     "no_of_sibling": [2,5,4,3,1]
# }
#
# df_rishta=pia.DataFrame(rishta)
# print(df_rishta)
#
# print(df_rishta[df_rishta["Prefered_caste"]=="pathan"])
# print(df_rishta)
# print(df_rishta[df_rishta["no_of_sibling"]>2])
# print(df_rishta)
# print(df_rishta[df_rishta["preferred_area"]=="dha"])
# print(df_rishta)
# print(df_rishta[(df_rishta["gender"]== "f") & (df_rishta["preferred_area"]== "nazimabad")])
# df_rishta["marreital_status"]=["single","divorce","widower","single","divorce"]
# df_rishta["nationality"]="pakistani"
# print(df_rishta)
# del df_rishta["profession"]

dishes = {
    "foodname" :["Pizza","Burger","Broast","Biryani","Shawarma","Pasta"],
    "price":[1000,500,700,300,250,150],
    "categoruy" : ["itlian","cheese","spicy","beef","turkish","italian"],
    "main_ingrediant" : ["feeta_bread","chicken","chicken","beef","marinated meat","white sauce"],
    "quantity" : [5,10,15,20,25,25],
    "status": ["available","not_available","available","available","not_available","not_available"]
}


df_resturent=pia.DataFrame(dishes)
print(df_resturent)

df_resturent["country"]="Pakistani"
print(df_resturent)

df_resturent["saleprice"]=[200,300,400,500,150,350]
print(df_resturent)

print(df_resturent[df_resturent["price"]>500])
print(df_resturent[df_resturent["status"]=="available"])
print(df_resturent[df_resturent["categoruy"]=="fastfood"])
print(df_resturent[df_resturent["foodname"]=="Biryani"])
print(df_resturent[(df_resturent["status"]=="available") & (df_resturent["price"]>1500)])

choice =input("Enter c -CSV\nj-JSON \nx -XML\ne -EXCEL")
if choice.lower()=="c":
    df_resturent.to_csv("mycsvfile.csv",index=False)
elif choice.lower()=="x":
    df_resturent.to_xml("myfile.xml")
elif choice.lower()=="j":
    df_resturent.to_xml("myfile.js")
elif choice.lower()=="e":
    df_resturent.to_xml("myfile.xlsx")
else:
    print("invalid input")