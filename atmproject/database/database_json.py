import json

import os 
fileloc = os.getcwd()
print(fileloc)
def write_json(data,filename = f"{fileloc}\database\data2.json"):
    with open(filename,'w') as f:
        json.dump(data , f, indent=4)

with open(f"{fileloc}\database\data2.json") as json_file:
    data = json.load(json_file)
    temp = data["customers"]
    y = {"id": len(temp)+1,"name": "yakup","password":32,"balance":8986589}
    temp.append(y)
write_json(data)