import json
import os
from datetime import datetime
from time import sleep
cwd=os.getcwd()
def get_data(path):
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError as err:
        print('File not found')
        new_dir=input('Enter full path of data file')
        return(get_data(new_dir))
    else:
        return data

def sort_task(data):
    return dict(sorted(data.items(),key=lambda x:x[1]))

def remove_expired_task():
    current_time=curr_time()
    expired_task=[]
    for i,j in data.items():
        if j<current_time:
            print(i,j)
            expired_task.append(i)
    for i in expired_task:
        print('pop',data.pop(i))
    print('after removing expired task',data)
    for key in data.keys():
        data[key]=data[key].replace(':','')


def time_difference(data):
    time_line=list()
    current_time=curr_time()
    current_time=current_time.replace(':','')
    current_time = datetime.strptime(current_time,"%H%M")
    print('nija',current_time,data)
    for i in data.values():
        print('-',i)
        diff=datetime.strptime(i,"%H%M")-current_time
        print(diff)
        time_line.append(diff.seconds)
        current_time=datetime.strptime(i,"%H%M")
    return time_line




"""
    find time difference and next and store in (key,next time) format 
    then get sleep for that time and 

"""


def curr_time():
    now = datetime.now()
    return now.strftime("%H:%M")
    

data = get_data(cwd+'\Todo\data.json')
print(data)
data=sort_task(data)
print('sorted data -->',data)
remove_expired_task()
time_line=time_difference(data)
print(time_line)
for i in range(len(time_line)):
    sleep(time_line[i])
    print('Hello BOii its time',curr_time())

"""
for i in range(20):
    time()
    sleep(5)
    
"""

