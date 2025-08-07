import pandas
import requests
from bs4 import BeautifulSoup

web_utl="https://www.pchotels.com/hotel-and-resort/pearl-continental-hotel-karachi?gad_source=1&gad_campaignid=22773155038&gbraid=0AAAAADMyAoh4BPCCqnNiRHO5vvdU-QYQt&gclid=EAIaIQobChMI4b-f6YXajgMV_aaDBx1jjhL2EAAYASAAEgKz0fD_BwE"
response=requests.get(web_utl)
data_uthao=BeautifulSoup(response.text,"html.parser")
h2_lao=data_uthao.find_all("div",class_="accomodation-content-bx")
Roomname,Description=[],[]
print(response)

for data in h2_lao:
    h3_lao=data.find_all("h3")
    p_lao = data.find_all("p")
    for a in h3_lao:
        Roomname.append((a.text))

    for p in p_lao:
        Description.append((p.text))

Room_Data={
"Roomname"   :Roomname,
"Description":Description
}

df=pandas.DataFrame(Room_Data)
print(df)
df.to_csv("Rooms_Data.csv",index=False)