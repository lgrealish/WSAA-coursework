# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 

# Author: Linda Grealish

from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"] # apikey contained in config.py

g = Github(apikey,verify = False) 

repo = g.get_repo("lgrealish/aprivateone") # url of repo

fileInfo = repo.get_contents("file.txt") # file that I want to update
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile,verify = False)
contentOfFile = response.text
print (contentOfFile)


# replacing Andrew with Linda in file.txt
string = contentOfFile
new_string = string.replace("Andrew", "Linda")
print(new_string)

# update file in github with commit message
gitHubResponse=repo.update_file(fileInfo.path,"amend Andrew to Linda and add new",newContents,fileInfo.sha)
print (gitHubResponse)