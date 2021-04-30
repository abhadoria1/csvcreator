import json
import logging
import csv

with open('data.json', 'r') as file_obj:
    setting = json.loads(file_obj.read())

access= setting['device']
access_in=access[0]
v1= access_in['tags']
value1=v1['cvg_sc']
timestp1 = value1['timestamp']
val1=value1['value']


value2=v1['cvo_sc']
timestp2 = value2['timestamp']
val2=value2['value']

value3=v1['cvw_sc']
timestp3 = value3['timestamp']
val3=value3['value']


value4=v1['qg_sc']
timestp4 = value4['timestamp']
val4=value4['value']


value5=v1['qo_sc']
timestp5 = value1['timestamp']
val5=value5['value']


value6=v1['qw_sc']
timestp6 = value6['timestamp']
val6=value6['value']

tag=['cvg_sc','cvo_sc','cvw_sc','qg_sc','qo_sc','qw_sc']
timestamp=[timestp1,timestp2,timestp3,timestp4,timestp5,timestp6]
value=[val1,val2,val3,val4,val5,val6]


print(tag)
print(timestamp)

with open('sim.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for x in range(0,6):
             writer.writerow([tag[x],timestamp[x],value[x]])

           

search = input("search by tag name or time stamp : ")

for i in range(0,6):
    if search==tag[i]:
        print('tag value searched:',value[i])
        break
    if search==timestamp[i]:
        print('tag value searched:',value[i])
        break



