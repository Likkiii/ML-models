# Pgm to perform K-Means Clustering Algorithm (without sklearn) 

# Import header files
import math
import numpy as np

# Enter no. of points
n = int(input("\nEnter the number of points: "))

# K value
k = 3

print("\nEnter the points: ")
# Input x values
x = []
print("\nEnter the x-values: ")
for i in range(n): 
    a = int(input())
    x.append(a) 
    
# Input y values
y = []
print("Enter the y-values: ")
for i in range(n): 
    b = int(input())
    y.append(b) 

points = np.column_stack((x, y))

# Taking first 3 cluster centers
mean = []
for i in range(k):
    mean.append(points[i])

# Manhattan distance
d = 1

# Find distance between points
def dist(a, b):
    return round(((math.fabs(a[0] - b[0])**d) + (math.fabs(a[1] - b[1])**d)) ** (1/d), 2)

# Calculate new means
def Mean(cdata):
    mean = []
    for i in cdata:
        x1, y1 = 0, 0
        for j in i:
            x1 += points[j][0]
            y1 += points[j][1]
        mean.append([round(x1/len(i), 2), round(y1/len(i), 2)])
    return mean

# Display table
def printCentres():
    clusters = [[] for _ in range(k)]
    for i in range(len(points)):
        cv, cl = 999, 0
        for j in range(k):
            dis = dist(points[i], mean[j])
            if dis < cv:
                cv, cl = dis, j
        clusters[cl].append(i)
    sv = -1
    # for i in clusters:
    #     print(f"["+",".join(f"" + str(points[j]) for j in i)+"]")
    for i in clusters:
        print(f"["+",".join(f"" + str(points[j]) for j in i)+"]")
    return clusters

# Print final clusters
prevCluster, currentCluster = [], printCentres()
while prevCluster != currentCluster:
    mean = Mean(currentCluster)
    prevCluster = currentCluster
else:
    print()

