# Distribution Analysis

def buildDistributionAnalysisDictionary(numbersList):
    """
    Receives a list of numbers and returns a dictionary where:
    - each key is a unique value from the list
    - each value is the percentage of elements in the list that are <= that key
    The dictionary is returned sorted by key.
    """
    totalElementCount = len(numbersList)

    # Sort the list so we can count how many values are <= each unique number
    sortedNumbersList = sorted(numbersList)

    distributionAnalysisDictionary = {}

    # Go through each unique value in sorted order
    for uniqueNumber in sorted(set(sortedNumbersList)):
        # Count how many elements are <= this uniqueNumber
        lessThanOrEqualToCount = 0
        for currentNumber in sortedNumbersList:
            if currentNumber <= uniqueNumber:
                lessThanOrEqualToCount += 1

        # Convert the count to a percentage
        percentageLessThanOrEqual = (lessThanOrEqualToCount / totalElementCount) * 100
        distributionAnalysisDictionary[uniqueNumber] = percentageLessThanOrEqual

    return distributionAnalysisDictionary

# Example Iinput Test Case
numbersList = [3, 1, 2, 3, 4, 2]
resultDictionary = buildDistributionAnalysisDictionary(numbersList)
print(resultDictionary)



