import pandas
import requests
from bs4 import BeautifulSoup

web_utl="https://www.nueplex.com/"
response=requests.get(web_utl)
data_uthao=BeautifulSoup(response.text,"html.parser")
h2_lao=data_uthao.find_all("table",class_="table")
Movie,Price=[],[]
print(response)

for data in h2_lao:
    tbody=data.find_all("tbody")

    for a in tbody:
        tr = a.find_all("tr")
        for tr in tr:
            th = tr.find_all("th")
            td = tr.find_all("td")
            for tth in th:
                Movie.append(tth)
            for tth in td:
                Price.append(tth)


Movie_Data={
"Movie"   :Movie,
"Price":Price
}

df=pandas.DataFrame(Movie_Data)
print(df)
df.to_csv("Movies_Data.csv",index=False)