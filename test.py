"""
from datetime import datetime,time,timedelta

a = '2200'
b = '1800'
time1 = datetime.strptime(a,"%H%M") # convert string to time
time2 = datetime.strptime(b,"%H%M") 
diff = time1 -time2
print(time1.hour)"""


a={'hello':'ninja'}
for i,j in a.items():
    j+='adasd'
print(a)

