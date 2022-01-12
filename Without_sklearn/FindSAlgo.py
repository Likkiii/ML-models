# Pgm to predict maximally specific hypothesis using Find S Algorithm (without scikit-learn)

num_attributes = int(input())
attributes = []
for i in range(num_attributes):
    attributes.append(input().split(" "))
    
num_data = int(input())
data = []
for i in range(num_data):
    data.append(input().split(" "))

print("\nThe most general hypothesis : ['?','?','?','?','?','?']")
print("The most specific hypothesis : ['0','0','0','0','0','0']")

print("\nThe given Training Data Set:")
print(data)

print("\nThe initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

# Comparing with First Training Example
for j in range(0, num_attributes):
    hypothesis[j] = data[0][j]

# Comparing with Remaining Training Examples of Given Data Set
print("\n Find S: Finding a Maximally Specific Hypothesis\n")
for i in range(0, len(data)):
    if data[i][num_attributes] == 'Yes':
        for j in range(0, num_attributes):
            if data[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = data[i][j]
    print(" For Training Example No :{0} the hypothesis is ".format(
        i), hypothesis)

print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)

# ----------------------------------------------------------------------------------------------------------
# Hardcoded input for testing

# data = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
#         ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
#         ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
#         ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

# attributes = [['Sunny', 'Rainy'],
#               ['Warm', 'Cold'],
#               ['Normal', 'High'],
#               ['Strong', 'Weak'],
#               ['Warm', 'Cool'],
#               ['Same', 'Change']]

# num_attributes = len(attributes)
# ----------------------------------------------------------------------------------------------------------
