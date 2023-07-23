import requests
from bs4 import BeautifulSoup
import pandas as pd

register_nos = ['71772116101', '71772116102', 
                '71772116103', '71772116104', 
                '71772116105', '71772116106', 
                '71772116107', '71772116108',  
                '71772116113', '71772116114', 
                '71772116115', '71772116116', 
                '71772116118', '71772116119', 
                '71772116120', '71772116121', 
                '71772116122', '71772116123', 
                '71772116126', '71772116127', 
                '71772116128', '71772116129', 
                '71772116130', '71772116131', 
                '71772116132', '71772116133', 
                '71772116134', '71772116135', 
                '71772116136', '71772116137', 
                '71772116138', '71772116139', 
                '71772116140', '71772116141', 
                '71772116142', '71772116143', 
                '71772116144', '71772116145', 
                '71772116146', '71772116147', 
                '71772116148', '71772116150', 
                '71772116151', '71772116152', 
                '71772116153', '71772116154', 
                '71772116155', '71772116L01', 
                '71772116L02', '71772116L03', 
                '71772116L04', '71772116L05', 
                '71772116L07', '71772116L08', 
                '71772116L09', '71772116L10', 
                '71772116L11', '71772116L12', 
                '71772116L13', '71772116L14', 
                '71772116L15', '71772116L16', 
                '71772116L17', '71772116L18']

url = "https://gct.ac.in/results"

headers = {
    'Cookie': 'SSESS04cdea5b4fc4a758d541ba851c3286c4=iLep6ekVUdpOr2Mdq4YhTJ5DmfCviNoNd-PbkjBlgYI; textsize=76'
    }

files=[]

full_result = pd.DataFrame()

for reg_no in register_nos:
    
    payload = {'reg_no': reg_no,
    'btn': 'Submit'}
    
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    soup = BeautifulSoup(response.text, 'html.parser')  
    table = soup.find_all('table')[-1].find_all('div')
    count = 1
    res = []
    sub = []
    for i in table:
        #print(i.text, end=" ")
        sub.append(i.text)
        if count == 5:
            res.append(sub)
            sub = []
            print("\n")
            count = 0
        count += 1

    result = pd.DataFrame(res)
    result['reg_no'] = reg_no
    print("Reading -> ", reg_no)

    full_result = full_result._append(result, ignore_index=True)

print(full_result)

full_result.to_csv("result-fourth-sem.csv", ignore_index=True)