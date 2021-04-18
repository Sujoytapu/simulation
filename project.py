# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:04:21 2021

@author: Asus
"""

from numpy import random

x = random.poisson(lam=5.6, size=19)

print(x)


y = random.exponential(scale=1, size=20)

print(y)

print(f"Interarrival Time: {x}")

a=0
b=0
arrival = [0]
while a<len(x):
    b=b+x[a]
    arrival.append(b)
    a=a+1


print(f"Arrival Time: {arrival}")

tsb = [0]
tse =[0+y[0]]
waiting = []
systime= []
idletime= [0]
c=1
d=0
while c<len(arrival):
  
    if tse[c-1]<arrival[c]:
        tsb.append(arrival[c])
    else:
        tsb.append(tse[c-1])
    waiting.append(tsb[c-1]-arrival[c-1])
    systime.append(tse[c-1]-arrival[c-1])
    if c>1:
        idletime.append(tsb[c]-tse[c-1])
    c=c+1
    tse.append(tsb[c-1]+y[c-1])
  
        
print(f"Time Service Begins: {tsb}")
print(f"Time Service Ends: {tse}")
print(f"Waiting Time: {waiting}")
print(f"The Customer Spends in System: {systime}")
print(f"Idle Time of Server: {idletime}")

    
print("|    Cust. | Inter Arrival | Arrival | Service | Service T. | Waiting T. | Service T. | C. Spend T. | Server   |")
print("|     No.  |  Time         |  Time   |  Time   |   Begin    |  in Queue  |   End      |  in System  | Idle T.  |")


for i in range(19):
    if i == 0:
        print(
            "|    %3i           -           %3i     %1f     %1.2f      %1.4f        %5.3f         %5.3f          -     |"
            % (i + 1, arrival[i], y[i], tsb[i], waiting[i], tse[i], systime[i]))
    else:
        print(
            "|    %3i         %3i           %3i     %1f     %1.2f      %1.4f        %5.3f         %5.3f       %5.3f  |"
            % (i + 1, x[i], arrival[i], y[i], tsb[i], waiting[i], tse[i], systime[i], idletime[i]))

    
z=0
f=0
while f<len(waiting):
    z=z+waiting[f]
    f=f+1
average=z/len(waiting)


print("the average waiting time is :",average)
    

   

  
    
    

    

    

