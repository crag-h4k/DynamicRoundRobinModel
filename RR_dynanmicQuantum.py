#usr/bin/env

#This is a model intended to demonstrate Round Robin
#process handling using Round Robin algorithm
#with importance sorting and dynamic quantum 

import random


numOfPs = input("How many proceses? ")
array1 = [] 
array2 = []
array3 = []

def getPriority():
    x = random.randint(1,3)
    return x
def getCPUBurst():
    y = round((random.randint(50,1000) +50), -1)
    return y

#process = {'PID':0,'priority':getPriority(),'CPUBurst':getCPUBurst()}

for i in range(numOfPs):
   
    arr = {'PID':i, 'priority':getPriority(), 'CPUBurst':getCPUBurst()}
    print arr
    
    if arr['PID'] == 1:
        array1.append(arr)
    elif arr['PID'] == 2:
        array2.append(arr)
    elif arr['PID'] == 3:
        array3.append(arr)

print "PID, Priority, CPU Burst"
print "First Priority Queue"
print array1
print "Second Priority Queue"
print array2
print "Third Priority Queue"
print array3
