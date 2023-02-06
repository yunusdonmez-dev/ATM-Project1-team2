import json

import os 
fileloc = os.getcwd()
print(fileloc)
def write_json(data,filename = r"C:\Users\yunus\OneDrive\Desktop\python ogreniyorum\ATM-Project\atmproject\atm_proje_file\data2.json"):
    with open(filename,'w') as f:
        json.dump(data , f, indent=4)

with open(r"C:\Users\yunus\OneDrive\Desktop\python ogreniyorum\ATM-Project\atmproject\atm_proje_file\data2.json") as json_file:
    data = json.load(json_file)
    temp = data["customers"]
    y = {"id": len(temp)+1,"name": "Tuba","password":"azra","balance":"99999"}
    temp.append(y)
write_json(data)