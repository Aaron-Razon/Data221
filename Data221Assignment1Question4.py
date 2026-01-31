# Sorted Search with Conditions

from random import random

# Create list of 20 random values between 0 and 1
randomValuesList = [random() for indexNumber in range(20)]

# Create random target value x between 0 and 1
targetValueX = random()

# Sort the list in ascending order
randomValuesList.sort()

# Collect all indices where the value is greater than or equal to x
matchingIndexList = []
for indexNumber in range(len(randomValuesList)):
    if randomValuesList[indexNumber] >= targetValueX:
        matchingIndexList.append(indexNumber)

# Print the sorted list and the target value
print("Sorted list: ", randomValuesList)
print("X: ", targetValueX)

# Print the first matching index (if one exists)
if len(matchingIndexList) > 0:
    print("First matching index: ", matchingIndexList[0])