# Pgm to predict a new sample using K-Nearest Neighbours Algorithm (without scikit-learn)

n = int(input("Enter number of rows:\n"))

train = []
for i in range(n):
    train.append(list(map(int, input(f"Enter point {i+1}:").split())))

test = list(map(int, input("\n\nEnter test data:").split()))

def distance(L, M):
    sum = 0
    for i,j in zip(L,M):
        sum += (i - j)**2
    return sum**0.5

def score(test: tuple, train: list):
    X = []
    for i in train:
        X.append([distance(test, i[:2]), i[2]])
    X.sort()
    return [x[-1] for x in X]

def KNN(test, train, n):
    L = score(test, train)[0:n]
    maxc = 0
    for i in list(set(L)):
        if L.count(i) > maxc:
            maxc = L.count(i)
    
    for i in L:
        if L.count(i) == maxc:
            return i

print("Classified as:", KNN(test, train, 3))