# Program that returns details of all trains in Ireland
# Author: Linda Grealish

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags = ['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction']
            

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# print (doc.toprettyxml())

#with open("trainxml.xml", "w") as xmlfp:
 # doc.writexml(xmlfp)

with  open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        #print (traincode)

        # now lets get everything
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        
        # instead of printing this you could output to another format
        #print (dataList)
        # for example a CSV file  
        train_writer.writerow(dataList)
