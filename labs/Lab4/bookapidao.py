import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url) 
print (response.json())

'''
def getallbooks():
  response = requests.get(url)
  return response.json()
'''