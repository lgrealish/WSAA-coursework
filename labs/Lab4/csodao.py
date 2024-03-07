import requests
import json

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
   with open("cso.json", "wt") as fp:
    print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset):
  url = urlBeginning + dataset + urlEnd
  response = requests.get(url)
  return response.json()

def getFormattedAsFile(datseet):
  pass

def getFormatted(dataset):
  data = getAll(dataset)
  ids = data["id"]
  values = data["value"]
  dimensions = data["dimension"]
  sizes = data["size"]
  valuecount = 0
  result = {}
  currentDict = result

  for dim0 in range(0, sizes[0]):
    currentId = ids[0]
    index = dimensions[currentId]["category"]["index"][dim0]
    label = dimensions[currentId]["category"]["label"][index]
    result[label] = {}
    currentDict = result[label]
    # print(label)
    for dim1 in range(0, sizes[1]):
      currentId = ids[1]
      index = dimensions[currentId]["category"]["index"][dim1]
      label = dimensions[currentId]["category"]["label"][index]
      print ("\t", label)
      for dim2 in range(0, sizes[2]):
        currentId = ids[2]
        index = dimensions[currentId]["category"]["index"][dim2]
        label = dimensions[currentId]["category"]["label"][index]
        print ("\t\t", label)
        for dim3 in range(0, sizes[3]):
          currentId = ids[3]
          index = dimensions[currentId]["category"]["index"][dim3]
          label = dimensions[currentId]["category"]["label"][index]
          print ("\t\t", label, " ", values[valuecount])
   



if __name__ == "__main__":
  #getAllAsFile("FP001")
  getFormatted("FP001")
