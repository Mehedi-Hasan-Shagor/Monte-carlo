#!/usr/bin/env python
# coding: utf-8

# In[3]:



import matplotlib.pyplot as plt
import random
import numpy as np
a=0
b=6
c=1
N=20
n=10
in_area=0
out_area=0
uncount=0
x1=[]
y1=[]
x2=[]
y2=[]
k=0
l=0
w=[[]]
print(w)
w[0].append(10)
print(w)
def f(x):
 return np.sin(x)
#for i in range(a,b,1):
count=0
for j in range(0,N,1):
        
    x=random.uniform(a, b/2)
    y=random.uniform(0, c)
    #print(j,x,y);
 
    if y<=f(x):
        count+=1
        in_area+=1
        plt.scatter(x,y,color="red")
        x1.append(x)
        y1.append(y)
    else:
        
        
        out_area+=1
        uncount+=1
        plt.scatter(x,y,color="blue")
       
print("Interval",count,uncount)
 
print("Number of point in range:",in_area)
print("Number of point out of range",out_area)
day=int(input("Enter the day"))
w1=np.linspace(a,b/2,day+1);
w= list(map(float, w1))
print(w1)

for i in range(len(w1)-1):
    w3=[]
    w4=[]
    d=0;
    d=int(d)
    
    for j in x1:
        if w1[i]<=j and w1[i+1]>=j:
            d=d+1
            
        
    print("day ",i+1,"=",d)
    w3.append(w1[i])
    w3.append(w1[i])
    w4.append(0)
    w4.append(f(w1[i]))
    plt.plot(w3,w4,color="green")
    

    

plt.title("Monte Carlo Method")
plt.xlabel("x")
plt.ylabel("f(x)")
x=np.linspace(a,b/2,1000)
plt.plot(x,f(x))
plt.plot([0,0,1,2,3,3],[0,1,1,1,1,0])
plt.grid()
plt.show()


# In[ ]:




