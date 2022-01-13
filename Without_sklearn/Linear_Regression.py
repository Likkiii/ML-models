# Pgm to predict a new sample using Linear Regression model (without scikit-learn)
import numpy as np

n = int(input("\nEnter the number of values: "))
X = []
print("\nEnter the x-values: ")
for i in range(n):
    a = int(input())
    X.append(a)
    
Y = []
print("Enter the y-values: ")
for i in range(n):
    b = int(input())
    Y.append(b)

# Calculate Mean of X & Y
xbar = np.mean(X)
ybar = np.mean(Y)


# Input test value
x = float(input("Enter the test value: "))

# Using the formula to calculate Slope & intercept
num = 0
den = 0
for i in range(n):
    num += (X[i] - xbar) * (Y[i] - ybar)
    den += (X[i] - xbar) ** 2

w1 = num / den
w0 = ybar - (w1 * xbar)

# Display Slope and Intercept
print("\nSlope: {:0.2f}".format(w1))
print("Intercept: {:0.2f}".format(w0))

# Predicting value from model (equation)
y_pred = (w1*x) + w0
print("Predicted value: {:0.2f}".format(y_pred))
