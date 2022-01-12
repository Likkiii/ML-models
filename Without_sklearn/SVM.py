# Pgm to predict a new sample using Support Vector Machine model (without scikit-learn)

import numpy as npy
import matplotlib.pyplot as plt

pos = []
pos_x = []
pos_y = []
np = int(input("\nEnter number of positive elements: ")) 
print("Enter positive data points separated by space")
for i in range(0, np): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    pos.append(ele) 
    pos_x.append(x)
    pos_y.append(y)
print(f"+ve data points: {pos}")

neg = []
neg_x = []
neg_y = []
nn = int(input("\nEnter number of negative elements: ")) 
print("Enter negative data points separated by space")
for i in range(0, nn): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    neg.append(ele)
    neg_x.append(x)
    neg_y.append(y)
print(f"-ve data points: {neg}")

plt.scatter(pos_x,pos_y,color='g')
plt.scatter(neg_x,neg_y,color='r')
plt.grid(True)
plt.show(block=False)

supvec = []
sv = int(input("\nEnter number of support vectors: ")) 
print("Enter support vector points separated by space")
for i in range(0, sv): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    supvec.append(ele) 


au = float(input("\nEnter number (bias) to be augmented to support vectors: "))
for i in range(0, sv): 
    supvec[i].append(au)
print(f"{supvec}\n")

A = [[4,7,6],[1,2,5],[9,3,8]]
B = npy.array([25, -10, -4]) 
ct=0

consts = []
for i in supvec:
    for j in supvec:
        temp = 0
        for k in range(0,len(supvec[0])):
            temp += i[k]*j[k]
        A[ct%3][ct//3]=temp
        ct+=1
        print(temp, end=" ")
    if(i[0:2] in pos):
        B[(ct-1)//3]=1
        print(" = 1")
    else:
        B[(ct-1)//3]=-1
        print(" = -1")
        
consts = npy.linalg.solve(A,B) 
print(f"\nConstants: {consts}")

interim = [0 for i in range(len(supvec))]
for i in range(0, len(supvec)):
    interim[i] = [consts[i]*x for x in supvec[i]]

print(interim)

final = []
for j in range(0,len(interim[0])):
    temp = 0
    for i in interim:
        temp += i[j]
    final.append(temp)
    
print(f"\nAnswer: {final}")
print(f"w = [{final[0]} , {final[1]}]")
print(f"b = {final[2]}")