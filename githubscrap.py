from pydriller import Repository
import pandas
import os.path

url=input("Please Enter Repositary Link :")
commitername,commiteremail,date,projectname,commitmsg=[],[],[],[],[]
print(f"Fetching {url}")
for a in Repository(url).traverse_commits():
   commitername.append(a.author.name)
   commiteremail.append(a.author.email)
   date.append(a.committer_date)
   projectname.append(a.project_name)
   commitmsg.append(a.msg)

print("Fetching Completed")
github_dict={
    "Project_name" : projectname,
    "Name" : commitername,
    "Email" : commiteremail,
    "Message" : commitmsg,
    "Date" : date

}
github_df=pandas.DataFrame(github_dict)

filename= input("Enter File Name")
if os.path.exists(f"{filename}.csv"):
    print(f"{filename} already exists ,Pleease choose different name")
else:
    github_df.to_csv(f"{filename}.csv",index=False)
    print("File created succe4sfully")