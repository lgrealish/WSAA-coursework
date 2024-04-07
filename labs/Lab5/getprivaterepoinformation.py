import requests
import json

filename = "repos-private.json"

url = 'https://github.com/lgrealish/aprivateone'

apikey = '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'

response = requests.get(url, auth=('token',apikey))  

print (response.status_code)

#print (response.json())  
with open(filename, 'w') as fp: 
  repoJSON = response.json() 
  json.dump(repoJSON, fp, indent=4) 